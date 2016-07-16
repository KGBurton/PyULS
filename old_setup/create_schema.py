#!/usr/bin/python
import os
import argparse
parser = argparse.ArgumentParser(description='Parse ULS file into SQLite.')
parser.add_argument('database', help='sqlite3 output database(WILL BE OVERWRITTEN)')
args = parser.parse_args()

if( os.path.isfile( args.database ) ):
	os.unlink(args.database)

import tempfile
commands = tempfile.NamedTemporaryFile(delete=False)
#print "schema builder:",commands.name
commands.write('attach database "' + args.database + '" as dbo;\n')

import urllib2
schema = urllib2.urlopen('http://wireless.fcc.gov/uls/ebf/pa_ddef49.txt')
for line in schema:
	commands.write(line)
commands.close()
os.system("cat "+commands.name+"|sqlite3")

os.unlink(commands.name)

