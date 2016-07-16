#!/usr/bin/python
import os
import argparse
parser = argparse.ArgumentParser(description='Parse ULS file into SQLite.')
parser.add_argument('database',   help='sqlite3 database to populate')
parser.add_argument('datfiles', nargs='+', help='list of DAT files to parse')
args = parser.parse_args()

import re
for dat in args.datfiles:
	dat_base = os.path.basename( dat)
	if re.search("[a-zA-Z0-9][a-zA-Z0-9].dat", dat_base):
		import tempfile
		dat_tmp = tempfile.NamedTemporaryFile(delete=False)
		dat_tmp.close()
		print ("Importing: "+dat)
		commands = tempfile.NamedTemporaryFile(delete=False)
		commands.write('attach database "' + args.database + '" as dbo;\n')
		os.system('cat ' + dat + ' | dos2unix | python lineparser.py > ' + dat_tmp.name )
		commands.write('.mode csv\n')
		commands.write('.separator "|"\n')
		commands.write('.import '+dat_tmp.name+' PUBACC_'+dat_base[0:2]+'\n')
		commands.close()
		os.system("cat "+commands.name+"|sqlite3")
		os.unlink(commands.name)
		os.unlink(dat_tmp.name)
	else:
		print "Unable to determine table name for "+dat
