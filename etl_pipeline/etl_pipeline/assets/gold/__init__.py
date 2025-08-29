from dagster import load_assets_from_modules


from . import dim_gold_job_skills

gold_assets = load_assets_from_modules ([
    dim_gold_job_skills
])