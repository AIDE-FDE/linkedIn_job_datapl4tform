from typing import Union
import pandas as pd
from dagster import IOManager, OutputContext, InputContext
from contextlib import contextmanager
import clickhouse_connect

# CLICKHOUSE_CONFIG = {
#     "host": "clickhouse",        
#     "port": 8123,                
#     "username": "admin",
#     "password": "admin123",
#     "database": "warehouse",
# }


@contextmanager
def connect_to_clickhouse(config):

    client = clickhouse_connect.get_client(
        host=config.get("host"),
        port=config.get("port", 8123),
        username=config.get("username"),
        password=config.get("password"),
        database=config.get("database"),
    )
    try:
        yield client
    finally:
        client.close()


class ClickHouseIOManager(IOManager):
    def __init__(self, config):
        self.config = config

    def _get_table_name(self, context: Union[InputContext, OutputContext]) -> str:
        """
        layer/schema/folder/table -> schema.table
        """
        layer, schema, folder, table = context.asset_key.path
        return f"{schema}.{table}"

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        table_name = self._get_table_name(context)

        if obj is None or obj.empty:
            context.log.warning(f"No data to insert into {table_name}")
            return

        with connect_to_clickhouse(self.config) as client:
            db_name = self.config.get("database")
            client.command(f"CREATE DATABASE IF NOT EXISTS {db_name}")

            cols = []
            for col, dtype in obj.dtypes.items():
                if pd.api.types.is_integer_dtype(dtype):
                    cols.append(f"{col} Int64")
                elif pd.api.types.is_float_dtype(dtype):
                    cols.append(f"{col} Float64")
                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    cols.append(f"{col} DateTime")
                else:
                    cols.append(f"{col} String")
            cols_str = ", ".join(cols)

            create_stmt = f"""
            CREATE TABLE IF NOT EXISTS {table_name} ({cols_str})
            ENGINE = MergeTree()
            ORDER BY tuple()
            """
            client.command(create_stmt)

            # insert dataframe
            client.insert_df(table_name, obj)

            context.log.info(f"Inserted {len(obj)} records into {table_name}")
            context.add_output_metadata({
                "table": table_name,
                "records": len(obj),
            })

    def load_input(self, context: InputContext) -> pd.DataFrame:
        table_name = self._get_table_name(context)
        with connect_to_clickhouse(self.config) as client:
            query = f"SELECT * FROM {table_name}"
            df = client.query_df(query)
        return df
