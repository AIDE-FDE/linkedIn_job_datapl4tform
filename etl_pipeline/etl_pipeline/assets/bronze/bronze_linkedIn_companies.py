# companies            
# company_industries   
# company_specialities 
# employee_counts 

import pandas as pd
from dagster import asset, Output


Tables = [
    "companies",            
    "company_industries",   
    "company_specialities", 
    "employee_counts" 
]

def create_bronze_asset (table_name: str):
    @asset (
        name=f"bronze_companies_{table_name}",
        key_prefix=["bronze", "linkedin", "companies"],  
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
    return bronze_asset


bronze_companies_companies = create_bronze_asset ("companies")
bronze_companies_company_industries = create_bronze_asset ("company_industries")
bronze_companies_company_specialities = create_bronze_asset ("company_specialities")