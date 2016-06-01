import pyuls
import functools
import fnmatch
import os

class ulsParser():
	pass

class ulsFolderParser(ulsParser):
	def __init__( self, path ):
		self.path = path
		self.parseMap = {}
		for file in os.listdir(path):
			if fnmatch.fnmatch(file, '??.dat'):
				fileCode = file[0:2]
				if( fileCode in pyuls.parsers ):
					self.parseMap[file] = functools.partial( pyuls.parse, fileCode )

	def parse( self, filename ):
		return self.parseMap[filename]( open( os.path.join( self.path, filename ), 'rb' ) )

class ulsFileParser(ulsParser):
	def __init__( self, path ):
		import os
		self.path = path
		self.parseMap = {}
		file = os.path.basename( path )
		fileCode = file[0:2]
		print fileCode
		if fileCode in pyuls.parsers:
			self.parseMap[file] = functools.partial( pyuls.parse, fileCode )

	def parse( self, filename ):
		return self.parseMap[filename]( open( self.path, 'rb' ) )

class ulsZipParser(ulsParser):
	def __init__( self, path ):
		import zipfile
		self.zip = zipfile.ZipFile( path )
		self.parseMap = {}
		for file in self.zip.infolist():
			file=file.filename
			if fnmatch.fnmatch(file, '??.dat'):
				fileCode = file[0:2]
				if fileCode in pyuls.parsers:
					self.parseMap[file] = functools.partial( pyuls.parse, fileCode )

	def parse( self, filename ):
		return self.parseMap[filename]( self.zip.open( filename , 'r' ) )

	def __del__( self ):
		self.zip.close()
