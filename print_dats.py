#!/usr/bin/python
import pyuls
import os
import pprint

for file in os.listdir("."):
	parseMap = {
		"AM.dat": pyuls.parseAM,
		"CO.dat": pyuls.parseCO,
		"EN.dat": pyuls.parseEN,
		"HD.dat": pyuls.parseHD,
		"HS.dat": pyuls.parseHS,
		"LA.dat": pyuls.parseLA,
		"SC.dat": pyuls.parseSC,
		"SF.dat": pyuls.parseSF,
		}

	if file in parseMap:
		pp = pprint.PrettyPrinter(indent=2)
		print "Printing",file
		for row in parseMap[file](open( file, 'rb' )):
			pp.pprint(row)

