#!/usr/bin/python

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]

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

def extract_sheet(ws):
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

def extract_sheets(wb):
	for sheet_name in wb.sheet_names():
		ws = wb.sheet_by_name(sheet_name)

		if( ws.name == "" ):
			"""Skip any empty sheets"""
			continue
		yield(sheet_name,list(extract_sheet(ws)))


import xlrd
for sheet in extract_sheets(xlrd.open_workbook('docs/pa_ddef42.xls')):
	print sheet
