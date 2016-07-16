#!/usr/bin/python
import argparse
parser = argparse.ArgumentParser(description='Creates indexes for ULS SQLite database.')
parser.add_argument('database',   help='sqlite3 database to index')
parser.add_argument('--index',      action='append', help='Index a specific column or columns. See example.index')
parser.add_argument('--index_file', action='append', help='Index definition file. See example.index')
args = parser.parse_args()

if not args.index_file:
	args.index_file=[]
if not args.index:
	args.index=[]

additional_indexes={}
for index_filename in args.index_file:
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

for index in args.index:
	columns = index.split(",")
	index_name = "__".join(columns)
	additional_indexes[index_name] = columns

import sqlite3
conn = sqlite3.connect(args.database)

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

conn.commit()
