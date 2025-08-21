1. Initialize the virtual environment then activate it
2. Download the dataset file


```
docker cp data/linkedin_23/ de_mysql:/tmp/
docker cp scripts/raw_mysql_linkedin23_schema.sql de_mysql:/tmp/


make to_mysql_root
SHOW GLOBAL VARIABLES LIKE 'LOCAL_INFILE';
SET GLOBAL LOCAL_INFILE=TRUE;
exit
```

```
make to_mysql
source /tmp/raw_mysql_linkedin23_schema.sql;


LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/companies.csv' INTO TABLE companies FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/company_industries.csv' INTO TABLE company_industries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/company_specialities.csv' INTO TABLE company_specialities FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/employee_counts.csv' INTO TABLE employee_counts FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/benefits.csv' INTO TABLE benefits FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/job_industries.csv' INTO TABLE job_industries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/job_skills.csv' INTO TABLE job_skills FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/salaries.csv' INTO TABLE salaries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/mappings/industries.csv' INTO TABLE industries FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
LOAD DATA LOCAL INFILE '/tmp/linkedin_23/mappings/skills.csv' INTO TABLE skills FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/postings.csv' INTO TABLE postings FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;


```

```sql
SET foreign_key_checks = 0;

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/companies.csv'
INTO TABLE companies
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(company_id, name, description, company_size, state, country, city, zip_code, address, url);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/company_industries.csv'
INTO TABLE company_industries
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(company_id, industry);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/company_specialities.csv'
INTO TABLE company_specialities
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(company_id, speciality);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/companies/employee_counts.csv'
INTO TABLE employee_counts
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(company_id, employee_count, follower_count, time_recorded);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/benefits.csv'
INTO TABLE benefits
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(job_id, inferred, benefit_type);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/job_industries.csv'
INTO TABLE job_industries
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(job_id, industry_id);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/job_skills.csv'
INTO TABLE job_skills
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(job_id, skill_abr);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/jobs/salaries.csv'
INTO TABLE salaries
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(salary_id, job_id, max_salary, med_salary, min_salary, pay_period, currency, compensation_type);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/mappings/industries.csv'
INTO TABLE industries
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(industry_id, industry_name);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/mappings/skills.csv'
INTO TABLE skills
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(skill_abr, skill_name);

LOAD DATA LOCAL INFILE '/tmp/linkedin_23/postings.csv'
INTO TABLE postings
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(job_id, company_name, title, description, max_salary, pay_period, location, company_id,
 views, med_salary, min_salary, formatted_work_type, applies, original_listed_time, remote_allowed,
 job_posting_url, application_url, application_type, expiry, closed_time, formatted_experience_level,
 skills_desc, listed_time, posting_domain, sponsored, work_type, currency, compensation_type,
 normalized_salary, zip_code, fips);

SET foreign_key_checks = 1;

```