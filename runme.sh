#!/bin/bash
DATABASE="uls.db"
INDEXFILE="example.index"

rm "$DATABASE"
./create_schema.sh "$DATABASE" && \
./fetch_databases.sh && \
./populate_databases.py "$DATABASE" `find databases -name *.dat` && \
./create_indexes.py "DATABASE" --index_file "$INDEXFILE" &&\
./optimize.sh "$DATABASE"
