import pyuls

class ulsParser():
	parseMap = {
		"AM.dat": pyuls.parseAM,
		"CO.dat": pyuls.parseCO,
		"EN.dat": pyuls.parseEN,
		"HD.dat": pyuls.parseHD,
		"HS.dat": pyuls.parseHS,
		"LA.dat": pyuls.parseLA,
		"SC.dat": pyuls.parseSC,
		"SF.dat": pyuls.parseSF,
		"SV.dat": pyuls.parseSV,
		"TP.dat": pyuls.parseTP,
		}

class ulsFolderParser(ulsParser):
	def __init__( self, path ):
		import os

		self.path = path
		self.parseMap = {}
		for file in os.listdir(path):
			if file in ulsParser.parseMap:
				self.parseMap[file] = ulsParser.parseMap[file]

	def parse( self, filename ):
		import os
		return self.parseMap[filename]( open( os.path.join( self.path, filename ), 'rb' ) )

class ulsFileParser(ulsParser):
	def __init__( self, path ):
		import os


		self.path = path
		self.parseMap = {}
		file = os.path.basename( path )
		if file in ulsParser.parseMap:
			self.parseMap[file] = ulsParser.parseMap[file]

	def parse( self, filename ):
		return self.parseMap[filename]( open( self.path, 'rb' ) )

class ulsZipParser(ulsParser):
	def __init__( self, path ):
		import zipfile
		self.zip = zipfile.ZipFile( path )
		self.parseMap = {}
		for file in self.zip.infolist():
			if file.filename in ulsParser.parseMap:
				self.parseMap[file.filename] = ulsParser.parseMap[file.filename]

	def parse( self, filename ):
		return self.parseMap[filename]( self.zip.open( filename , 'r' ) )

	def __del__( self ):
		self.zip.close()