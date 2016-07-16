#!/usr/bin/python

additional_indexes={}
index_filename = 'index_columns.txt'
with open(index_filename) as f:
	line_no = 0
	for line in f:
		line_no = line_no + 1
		try:
			short_line = line.rstrip()
			if( len(short_line) > 0 and short_line[0]!="#" ):
				columns = short_line.split(",")
				index_name = "__".join(columns)
				additional_indexes[index_name]=columns
		except:
			import sys
			print "While parsing: ", index_filename
			print "Unexpected error: ", sys.exc_info()[0]
			print "On line number: ", line_no, ":", line
			raise

#At this point, all data is loaded.
import sqlite3
conn = sqlite3.connect('uls.db')

import sys
if( sys.maxsize > 2**32 ):
	#Let's get this show on the road.
	#conn.execute("PRAGMA cache_size=-4000000");
	#Gotta go fast
	conn.execute("PRAGMA mmap_size=-1000000");
	pass
else:
	#Maybe not quite as fast...hope you have at least 512MB.
	conn.execute("PRAGMA cache_size=-268435456");
	conn.execute("PRAGMA mmap_size=134217728");

existing_tables={}
for table in conn.execute('select name from sqlite_master where type="table"'):
	tablename=table[0]
	columns=set()
	#sql injection here
	for column in conn.execute("PRAGMA table_info('" + tablename + "')"):
		columns.add(column[1])
	#print tablename,columns
	existing_tables[tablename]=columns

existing_indexes=set()
for row in conn.execute('select name from sqlite_master where type="index"'):
	existing_indexes.add(row[0])
#	print row[0]

for table in existing_tables:
#	print table,existing_tables[table]
	for index in additional_indexes:
#		print "\t",index,additional_indexes[index]
		table_index = table+"__"+index
		if table_index in existing_indexes:
			print "Skipping existing index:",table_index
			continue
		if existing_tables[table].issuperset( additional_indexes[index] ):
			print "Creating index:",table_index
			conn.execute("CREATE INDEX " + table_index + " ON " + table + "(" + ",".join(additional_indexes[index]) +");")
			existing_indexes.add(table_index)

print "Optimizing Database"
#conn.execute("VACUUM");

conn.commit()
