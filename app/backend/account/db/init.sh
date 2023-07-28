cat functions/*.sql > functions.sql
cat tables/*.sql > tables.sql


psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f tables.sql
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f functions.sql

