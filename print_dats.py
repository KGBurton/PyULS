#!/usr/bin/python
import pyuls
import os
import pprint

for file in os.listdir("."):
	parseMap = {
		"A2.dat": pyuls.parseA2,
		"AD.dat": pyuls.parseAD,
		"AM.dat": pyuls.parseAM,
		"CG.dat": pyuls.parseCG,
		"CO.dat": pyuls.parseCO,
		"EN.dat": pyuls.parseEN,
		"FA.dat": pyuls.parseFA,
		"HD.dat": pyuls.parseHD,
		"HS.dat": pyuls.parseHS,
		"LA.dat": pyuls.parseLA,
		"MW.dat": pyuls.parseMW,
		"RE.dat": pyuls.parseRE,
		"SC.dat": pyuls.parseSC,
		"SF.dat": pyuls.parseSF,
		"SH.dat": pyuls.parseSH,
		}

	if file in parseMap:
		pp = pprint.PrettyPrinter(indent=2)
		print "Printing",file
		for row in parseMap[file](open( file, 'rb' )):
			pp.pprint(row)

