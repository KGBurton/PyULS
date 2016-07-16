import os
import argparse
parser = argparse.ArgumentParser(description='Parse ULS file into SQLITTE.')
parser.add_argument('database', help='sqlite3 output database(WILL BE OVERWRITTEN)')
parser.add_argument('datfiles', nargs='+', help='list of DAT files to parse')
args = parser.parse_args()
#print args.database
#print args.datfiles

os.unlink(args.database)

import tempfile
commands = tempfile.NamedTemporaryFile(delete=False)
print "schema builder:",commands.name
commands.write('attach database "' + args.database + '" as dbo;\n')

import urllib2
schema = urllib2.urlopen('http://wireless.fcc.gov/uls/ebf/pa_ddef49.txt')
for line in schema:
	commands.write(line)
commands.close()
os.system("cat "+commands.name+"|sqlite3")

import re
dat_tmps = []
for dat in args.datfiles:
	dat_base = os.path.basename( dat)
	if re.search("[A-Z][A-Z].dat", dat_base):
		dat_tmp = tempfile.NamedTemporaryFile(delete=False)
		dat_tmp.close()
		print ("Found:"+dat+". Storing converted data in "+dat_tmp.name)
		dat_tmps.append( dat_tmp )
		commands = tempfile.NamedTemporaryFile(delete=False)
		commands.write('attach database "' + args.database + '" as dbo;\n')
		os.system('cat ' + dat + ' | dos2unix | python lineparser.py > ' + dat_tmp.name )
		commands.write('.mode csv\n')
		commands.write('.separator "|"\n')
		commands.write('.import '+dat_tmp.name+' PUBACC_'+dat_base[0:2]+'\n')
		commands.close()
		os.system("cat "+commands.name+"|sqlite3")
	else:
		print "Unable to determine table name for "+dat

os.unlink(commands.name)
for dat_tmp in dat_tmps:
	os.unlink( dat_tmp.name )
