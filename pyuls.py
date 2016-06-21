#!/usr/bin/env python

import csv
"""The purpose of this module is to parse each FCC
ULS database type into corresponding python types"""

def tryConvertString( input ):
	"""
	Try some different string encodings.
	Hopefully someday we can find the standard the FCC uses.
	I asked them, but I don't think they understood the question.
	"""
	for conversion in [ 'iso_8859_1', 'cp1252', 'utf-8' ]:
		try:
			return unicode(input, conversion, 'strict' )
		except UnicodeDecodeError:
			pass
	return unicode( input, 'iso_8859_1', 'ignore' )

parsers={}

from functools import partial
def parse( tableKey, fileLikeObject ):
	"""Map a key list onto a CSV file and do some conversions"""
	keys = parsers[tableKey][1]
	for row in csv.reader(fileLikeObject, delimiter='|'):
		yield dict(zip(keys, row))


import schema_parser
for sheet in schema_parser.extract_tables("docs/pa_ddef42.xls"):
	names=[]
	for row in sheet[2]:
		names.append(row[1])
	parsers[sheet[0]]=(sheet[1],names)
