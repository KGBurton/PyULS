#!/usr/bin/python
import pyuls
import os
import pprint
import fnmatch
pp = pprint.PrettyPrinter(indent=2)

for file in os.listdir("."):
	if fnmatch.fnmatch(file, '??.dat'):
		print "Printing",file
		fileCode = file[0:2]
		if( fileCode in pyuls.parsers ):
			for row in pyuls.parse(fileCode,open( file, 'rb' )):
				pp.pprint(row)

