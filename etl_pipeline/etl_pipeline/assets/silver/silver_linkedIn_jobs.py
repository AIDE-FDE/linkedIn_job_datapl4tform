from doctest import master
from dagster import asset, Output, AssetIn, AssetKey, AssetExecutionContext
import pandas as pd

from pyspark.sql.functions import regexp_replace
from pyspark.sql import SparkSession


# job_skills 
@asset (
    ins= {
        'bronze_jobs_job_skills': AssetIn (key_prefix=["bronze", "linkedin", "jobs"])
    },
    name='silver_jobs_job_skills',
    io_manager_key='minio_io_manager',
    key_prefix=["silver", "linkedin", "jobs"],
    group_name='silver',
    compute_kind='Spark'
)
def silver_job_skills_asset (
    context: AssetExecutionContext,
    bronze_jobs_job_skills: pd.DataFrame
) -> Output[pd.DataFrame]:
    spark = (
        SparkSession.builder.appName ('silver_jobs_job_skills')
                            .master ("spark://spark-master:7077")
                            .getOrCreate ()
    )

    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
    spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")

    bronze_jobs_job_skills_df = spark.createDataFrame (bronze_jobs_job_skills)

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
@asset (
    ins= {
        'bronze_jobs_job_industries': AssetIn (key_prefix=["bronze", "linkedin", "jobs"])
    },
    name='silver_jobs_job_industries',
    io_manager_key='minio_io_manager',
    key_prefix=["silver", "linkedin", "jobs"],
    group_name='silver',
    compute_kind='pandas'
)
def silver_job_industries_asset (
    context: AssetExecutionContext,
    bronze_jobs_job_industries: pd.DataFrame
) -> Output[pd.DataFrame]:
    pandas_df = bronze_jobs_job_industries.copy ()

    context.log.info (f'clean {len (pandas_df)} records to silver layer')

    return Output (
        pandas_df,
        metadata={
            'table': 'silver_jobs_job_skills',
            'record': len (pandas_df)
        }
    )