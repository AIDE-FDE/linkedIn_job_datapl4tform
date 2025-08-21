# postings

from dagster import asset, Output
import pandas as pd

table_name = "postings"
@asset (
    name=f"bronze_mapping_{table_name}",
    key_prefix=["bronze", "linkedin", "mapping"],  
    io_manager_key="minio_io_manager",
    required_resource_keys={"mysql_io_manager"},
    compute_kind="MySQL",
    group_name="bronze"
)
def bronze_asset (context) -> Output[pd.DataFrame]:
    sql = f"SELECT * FROM {table_name}"
    df = context.resources.mysql_io_manager.extract_data(sql)
    context.log.info(f"Extracted {len(df)} rows from MySQL table: {table_name}")
    context.log.info (df.head (10))
    return Output(
        df,
        metadata={
            "source_table": table_name,
            "records": len(df),
        }
    )
