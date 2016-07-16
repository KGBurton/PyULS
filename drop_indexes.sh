if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters. Please supply path to database"
	exit 1
fi

sqlite3 "$1" "select name from sqlite_master where type='index';" | sed -e 's/^/drop index /' | sed -e 's/$/;/' | sqlite3 "$1"
