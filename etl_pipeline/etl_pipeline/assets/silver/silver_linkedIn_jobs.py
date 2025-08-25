from dagster import asset, Output, AssetIn, AssetKey, AssetExecutionContext
import pandas as pd

from pyspark.sql.functions import regexp_replace


# job_skills 
@asset (
    ins= {
        'bronze_jobs_job_skills': AssetIn (key_prefix=["bronze", "linkedin", "jobs"])
    },
    name='silver_jobs_job_skills',
    io_manager_key='minio_io_manager',
    required_resource_keys={'spark'},
    key_prefix=["silver", "linkedin", "jobs"],
    group_name='silver',
    compute_kind='Spark'
)
def silver_job_skills_asset (
    context: AssetExecutionContext,
    bronze_jobs_job_skills: pd.DataFrame
) -> Output[pd.DataFrame]:
    spark = context.resources.spark

    bronze_jobs_job_skills_df = spark.createDataframe (bronze_jobs_job_skills)

    cleaned_df = bronze_jobs_job_skills_df.withColumn (
        "skill_abr",
        regexp_replace("skill_abr", "[\r\n]", "")
    )

    pandas_df = cleaned_df.toPandas ()

    context.log.info (f'clean {len (pandas_df)} records to silver layer')

    return Output (
        pandas_df,
        metadata={
            'table': 'silver_jobs_job_skills',
            'record': len (pandas_df)
        }
    )



# benefits             
# industries           
# job_industries       