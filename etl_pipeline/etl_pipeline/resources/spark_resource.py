from dagster import resource
from pyspark.sql import SparkSession

@resource (config_schema={
    'app_name': str,
    'master_url': str
})
def spark_resource (init_context):
    app_name = init_context.resource_config["app_name"]
    master_url = init_context.resource_config["master_url"]

    spark = SparkSession.builder \
        .appName(app_name) \
        .master(master_url) \
        .getOrCreate()

    try:
        yield spark
    
    finally:
        pass