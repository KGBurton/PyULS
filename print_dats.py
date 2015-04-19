#!/usr/bin/python
import pyuls
import os
import pprint

for file in os.listdir("."):
	parseMap = {
		"A2.dat": pyuls.parseA2,
		"AD.dat": pyuls.parseAD,
		"AM.dat": pyuls.parseAM,
		"BC.dat": pyuls.parseBC,
		"CG.dat": pyuls.parseCG,
		"CO.dat": pyuls.parseCO,
		"EN.dat": pyuls.parseEN,
		"FA.dat": pyuls.parseFA,
		"HD.dat": pyuls.parseHD,
		"HS.dat": pyuls.parseHS,
		"LA.dat": pyuls.parseLA,
		"LM.dat": pyuls.parseLM,
		"MI.dat": pyuls.parseMI,
		"MW.dat": pyuls.parseMW,
		"RE.dat": pyuls.parseRE,
		"SC.dat": pyuls.parseSC,
		"SE.dat": pyuls.parseSE,
		"SF.dat": pyuls.parseSF,
		"SH.dat": pyuls.parseSH,
		"SR.dat": pyuls.parseSR,
		"SV.dat": pyuls.parseSV,
		"TP.dat": pyuls.parseTP,
		}

	if file in parseMap:
		pp = pprint.PrettyPrinter(indent=2)
		print "Printing",file
		for row in parseMap[file](open( file, 'rb' )):
			pp.pprint(row)

