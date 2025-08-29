from dagster import load_assets_from_modules


from . import dim_gold_job_skills
from . import dim_gold_job_industries

gold_assets = load_assets_from_modules ([
    dim_gold_job_skills,
    dim_gold_job_industries
])