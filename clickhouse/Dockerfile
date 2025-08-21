FROM clickhouse/clickhouse-server:latest

COPY config/config.xml /etc/clickhouse-server/config.xml
COPY config/users.xml /etc/clickhouse-server/users.xml
COPY init/init.sql /docker-entrypoint-initdb.d/init.sql