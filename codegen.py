#!/usr/bin/python
import xlrd
workbook = xlrd.open_workbook('docs/pa_ddef42.xls')

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
	return row_compare( ws, row, [ "", "", "" ] )

for sheet_name in workbook.sheet_names():
	worksheet = workbook.sheet_by_name(sheet_name)
	table_name = worksheet.cell_value(0,0)

	print "table:",worksheet.name
	if( table_name == "" ):
		"""Skip any empty sheets"""
		continue

	row_offset = 0
	if( is_header(worksheet,1) ):
		row_offset = 1
	elif( is_header(worksheet,2) ):
		row_offset = 2
	print worksheet.cell_value(row_offset,0),table_name
	for row in xrange( row_offset + 1, worksheet.nrows ):
		if( row_is_empty(worksheet,row) ):
			continue
		field_id = int( worksheet.cell_value( row, 0 ) )
		field_name = worksheet.cell_value( row, 1 )
		field_type = worksheet.cell_value( row, 2 )
		if( row == row_offset + 1 ):
			field_name = field_name.replace( "[" + worksheet.name + "]", "" )
		field_name = field_name.rstrip()
		print field_id,field_name,field_type
