#!/bin/bash

rm -rf databases
mkdir -p databases

WT_DB_LIST=""
DB_LIST=""
for DB in `( curl -s wireless.fcc.gov/uls/data/complete/index2.htm && curl -s wireless.fcc.gov/uls/data/complete/index.htm ) | grep "A HREF=\"[al]_[a-zA-Z0-9]*.zip" | cut -d ">" -f "2" | cut -d "<" -f 1 | sort`
do
	DB_LIST="$DB_LIST $DB"
	if [[ ${DB:0:2} == "a_" ]]
	then
		WT_DB_LIST="$WT_DB_LIST $DB Applications off"
	elif [[ ${DB:0:2} == "l_" ]]
	then
		WT_DB_LIST="$WT_DB_LIST $DB Licenses off"
	else
		WT_DB_LIST="$WT_DB_LIST $DB Unknown off"
	fi

done

command -v whiptail >/dev/null 2>&1
if [ $? -eq 0 ]
then
	whiptail \
		--title "Select FCC databases to fetch" \
		--checklist \
			--separate-output \
			--notags \
		"Please pick some" 20 72 15 \
		$WT_DB_LIST \
		2>databases/list
else
	echo "Whiptail not found, downloading full set:"
	echo "$DB_LIST" | tee databases/list
fi

while read DB
do
	(
	echo "Fetching $DB..." &&
	wget --quiet -P databases "http://wireless.fcc.gov/uls/data/complete/$DB" &&
	echo "...extracting $DB..." &&
	mkdir "databases/$DB.extracted" &&
	unzip -q "databases/$DB" -d "databases/$DB.extracted" &&
	echo "...extracted $DB"
	) &
done < databases/list

wait
