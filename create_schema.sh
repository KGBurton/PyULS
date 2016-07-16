if [ "$#" -ne 1 ]; then
    echo "Illegal number of parameters. Please supply path to database"
	exit 1
fi

( echo "attach database \"$1\" as dbo;" && curl http://wireless.fcc.gov/uls/ebf/pa_ddef49.txt ) | sqlite3 "$1"
