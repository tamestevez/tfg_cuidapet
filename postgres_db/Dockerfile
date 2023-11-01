FROM postgres:14.1
COPY postgres_db/initdb_cuidapet.sh /docker-entrypoint-initdb.d/
RUN chmod 0755 /docker-entrypoint-initdb.d/initdb_cuidapet.sh

ENV PGDATA /var/lib/postgresql/data
VOLUME /var/lib/postgresql/data
