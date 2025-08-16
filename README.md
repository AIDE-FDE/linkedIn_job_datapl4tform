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