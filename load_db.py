#!/usr/bin/python
import csv

# a generator that extracts relevant fields from a pipe-separated ULS EN.dat file
def operators(filename):
	with open(filename,'rb') as csvfile:
		csvreader = csv.reader(csvfile, delimiter='|')
		for row in csvreader:
			callsign = row[4]
			fullname = unicode(row[7], '8859', "ignore")
			firstname = unicode(row[8], '8859', "ignore")
			lastname = unicode(row[10], '8859', "ignore")
			address = unicode(row[15], '8859', "ignore")
			city = row[16]
			state = row[17]
			zip = row[18]
			print firstname,lastname
			yield(callsign,firstname,lastname,address,city,state,zip)

import sqlite3

conn = sqlite3.connect('uls.db')
conn.isolation_level = None

c = conn.cursor()
c.execute("begin")
c.execute('''CREATE TABLE IF NOT EXISTS operators
	(callsign TEXT,
	fname TEXT,
	lname TEXT,
	address TEXT,
	city TEXT,
	state TEXT,
	zip INT)''')

c.executemany("INSERT INTO operators VALUES(?,?,?,?,?,?,?)", operators('EN.dat') )

c.execute("commit")
