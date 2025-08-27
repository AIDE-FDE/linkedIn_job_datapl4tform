from dagster import asset, Output, AssetIn, AssetKey, AssetExecutionContext
import pandas as pd

from pyspark.sql.functions import regexp_replace, regexp_extract, when, col
from pyspark.sql import SparkSession

# companies            
# company_industries
@asset (
    ins= {
        'bronze_companies_company_industries': AssetIn (key_prefix=["bronze", "linkedin", "companies"])
    },
    name='silver_companies_company_industries',
    io_manager_key='minio_io_manager',
    key_prefix=["silver", "linkedin", "companies"],
    group_name='silver',
    compute_kind='Spark'
)
def silver_companies_company_industries (
    context: AssetExecutionContext,
    bronze_companies_company_industries: pd.DataFrame
) -> Output[pd.DataFrame]:
    spark = (
        SparkSession.builder.appName ('silver_companies_company_industries')
                            .master ("spark://spark-master:7077")
                            .getOrCreate ()
    )

    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")

    bronze_companies_company_industries_df = spark.createDataFrame (bronze_companies_company_industries)
    bronze_companies_company_industries_df.createOrReplaceTempView ('company_industries')


    sql_stm = """
        SELECT
            company_id,
            CASE
                WHEN REGEXP_EXTRACT(industry, '"([^"]+)"', 1) != '' 
                THEN REGEXP_EXTRACT(industry, '"([^"]+)"', 1)
                ELSE industry
            END AS industry
        FROM company_industries
    """

    cleaned_df = spark.sql (sql_stm)

    context.log.info(f"Spark count before remove duplicate: {cleaned_df.count()}")

    cleaned_df = cleaned_df.dropDuplicates(["company_id", "industry"])

    context.log.info(f"Spark count before toPandas: {cleaned_df.count()}")

    pandas_df = cleaned_df.toPandas()
    context.log.info(f"Pandas shape: {pandas_df.shape}")


    context.log.info (f'clean {len (pandas_df)} records to silver layer')

    return Output (
        pandas_df,
        metadata={
            'table': 'company_industries',
            'record': len (pandas_df),
            'column': list (pandas_df.columns)
        }
    )  
# company_specialities 
# employee_counts 
