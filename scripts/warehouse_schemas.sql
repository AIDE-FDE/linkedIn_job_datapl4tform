CREATE DATABASE IF NOT EXISTS warehouse 


-- companies
DROP TABLE IF EXISTS warehouse.companies;
CREATE TABLE warehouse.companies (
    company_id UInt64,
    name Nullable(String),
    description Nullable(String),
    state Nullable(String),
    country Nullable(String),
    city Nullable(String),
    zip_code Nullable(String),
    address Nullable(String),
    url Nullable(String)
)
ENGINE = MergeTree
ORDER BY company_id;

-----------------------------------------

-- company_industries
DROP TABLE IF EXISTS warehouse.company_industries;
CREATE TABLE warehouse.company_industries (
    company_id UInt64,
    industry_id UInt64,
    industry_name Nullable(String)
)
ENGINE = MergeTree
ORDER BY (company_id, industry_id);

-----------------------------------------
-- company_specialities
DROP TABLE IF EXISTS warehouse.company_specialities;
CREATE TABLE warehouse.company_specialities (
    company_id UInt64,
    speciality Nullable(String)
)
ENGINE = MergeTree
ORDER BY (company_id);
-------------------------------------------
-- employee_counts
DROP TABLE IF EXISTS warehouse.employee_counts;
CREATE TABLE warehouse.employee_counts (
    company_id UInt64,
    employee_count Nullable(Int32),
    follower_count Nullable(UInt64),
    time_recorded UInt64 -- Unix timestamp
)
ENGINE = MergeTree
ORDER BY (company_id);

------------------------------------------

-- postings
DROP TABLE IF EXISTS warehouse.postings;
CREATE TABLE warehouse.postings (
    job_id UInt64,
    company_name Nullable(String),
    title Nullable(String),
    description Nullable(String),
    location Nullable(String),
    company_id Nullable(UInt64),
    views Nullable(UInt64),
    formatted_work_type Nullable(String),
    applies Nullable(Int32),
    original_listed_time Nullable(UInt64),
    remote_allowed Nullable(UInt8), -- tinyint(1) → UInt8
    job_posting_url Nullable(String),
    application_url Nullable(String),
    application_type Nullable(String),
    expiry Nullable(UInt64),
    closed_time Nullable(UInt64),
    formatted_experience_level Nullable(String),
    skills_desc Nullable(String),
    listed_time Nullable(UInt64),
    posting_domain Nullable(String),
    sponsored Nullable(UInt8) DEFAULT 0,
    work_type Nullable(String),
    normalized_salary Nullable(Decimal(15,2)),
    zip_code Nullable(String),
    fips Nullable(String)
)
ENGINE = MergeTree
ORDER BY job_id;

-- benefits
DROP TABLE IF EXISTS warehouse.benefits;
CREATE TABLE warehouse.benefits (
    job_id UInt64,
    inferred Nullable(UInt8) DEFAULT 0, -- boolean
    benefit_type Nullable(String)
)
ENGINE = MergeTree
ORDER BY job_id;

-----------------------------------------------------

-- job_industries
DROP TABLE IF EXISTS warehouse.job_industries;
CREATE TABLE warehouse.job_industries (
    job_id UInt64,
    industry_id UInt64,
    industry_name Nullable(String)

)
ENGINE = MergeTree
ORDER BY (job_id, industry_id);

-------------------------------------------------------


-- job_skills
DROP TABLE IF EXISTS warehouse.job_skills;
CREATE TABLE warehouse.job_skills (
    job_id UInt64,
    skill_abr String,
    skill_name Nullable(String)
)
ENGINE = MergeTree
ORDER BY (job_id, skill_abr);

------------------------------------------------------

-- salaries
DROP TABLE IF EXISTS warehouse.salaries;
CREATE TABLE warehouse.salaries (
    salary_id UInt64,
    job_id UInt64,
    max_salary Nullable(Decimal(15,2)),
    med_salary Nullable(Decimal(15,2)),
    min_salary Nullable(Decimal(15,2)),
    pay_period Nullable(String),
    currency Nullable(String),
    compensation_type Nullable(String)
)
ENGINE = MergeTree
ORDER BY (salary_id, job_id);
