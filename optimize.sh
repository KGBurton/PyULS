if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters. Please supply path to database"
	exit 1
fi

sqlite3 "$1" "VACUUM;"
