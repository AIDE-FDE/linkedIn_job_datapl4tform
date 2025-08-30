CREATE DATABASE metabase_db;

CREATE USER metabase_user WITH ENCRYPTED PASSWORD 'metabase_admin123';

GRANT ALL PRIVILEGES ON DATABASE metabase_db TO metabase_user;


GRANT ALL PRIVILEGES ON DATABASE metabase_db TO metabase_user;

GRANT USAGE ON SCHEMA public TO metabase_user;

GRANT CREATE ON SCHEMA public TO metabase_user;

ALTER SCHEMA public OWNER TO metabase_user;
