1. Initialize the virtual environment then activate it
2. Download the dataset file


```
docker cp data/linkedin_23/ de_mysql:/tmp/
docker cp scripts/raw_mysql_linkedin23_schema.sql de_mysql:/tmp/
docker cp scripts/load_data.sql de_mysql:/tmp/



make to_mysql_root
SHOW GLOBAL VARIABLES LIKE 'LOCAL_INFILE';
SET GLOBAL LOCAL_INFILE=TRUE;
exit
```

```
make to_mysql
source /tmp/raw_mysql_linkedin23_schema.sql;
source /tmp/load_data.sql;

```

```sql


```



repair


docker cp postings_repair.csv de_mysql:/tmp/
docker cp scripts/update_postings.sql de_mysql:/tmp/
make to_mysql
source /tmp/update_postings.sql;



![Alt text](./images/lineage.svg)
