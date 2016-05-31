#!/usr/bin/python

def row_compare( ws, row, cols ):
	col_idx = 0
	for col in cols:
		if( col != ws.cell_value( row, col_idx) ):
			return False
		col_idx+=1
	return True

def is_header(ws,row):
	return row_compare( ws, row, [ "Position", "Data Element", "Definition" ] )

def row_is_empty(ws,row):
	if( row_compare( ws, row, [ "", "", "" ] ) ): return True
	if( row_compare( ws, row, [ "", "", " " ] ) ): return True
	if( row_compare( ws, row, [ "", "x", "" ] ) ): return True
	return False

def extract_table(ws):
	row_offset = 0
	if( is_header(ws,1) ):
		row_offset = 1
	elif( is_header(ws,2) ):
		row_offset = 2

	for row in xrange( row_offset + 1, ws.nrows ):
		if( row_is_empty(ws,row) ):
			continue

		field_position = int( ws.cell_value( row, 0 ) )
		field_data_element = ws.cell_value( row, 1 )
		field_definition = ws.cell_value( row, 2 )
		if( row == row_offset + 1 ):
			field_data_element = field_data_element.replace( "[" + ws.name + "]", "" )
		yield(field_position,field_data_element.rstrip(),field_definition)

def extract_tables(filename):
	import xlrd
	wb = xlrd.open_workbook(sys.argv[1])
	for sheet_name in wb.sheet_names():
		ws = wb.sheet_by_name(sheet_name)

		if( ws.name == "" ):
			"""Skip any empty sheets"""
			continue
		yield(sheet_name,ws.cell_value(0,0),list(extract_table(ws)))

if __name__ == "__main__":
	def camelCase(st):
	    output = ''.join(x for x in st.title() if x.isalpha())
	    return output[0].lower() + output[1:]

	import sys
	if( len(sys.argv) > 1 ):
		file=sys.argv[1]

		for sheet in extract_tables(sys.argv[1]):
			print sheet[0],":",sheet[1]
			for x in sheet[2]:
				print "\t",camelCase(x[1].encode('utf-8')),":",x[2]
	else:
		print "Usage:",sys.argv[0],"path-to-excel-schema"
