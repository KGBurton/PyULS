#!/usr/bin/python
import argparse
import ioapi
import pprint

parser = argparse.ArgumentParser(description='Print ULS contents')
parser.add_argument('paths', metavar='path', nargs='+',
                   help='path to a ULS database in folder, zip, or filename form')

args = parser.parse_args()
pp = pprint.PrettyPrinter(indent=2)

for path in args.paths:
	if path.endswith('.dat'):
		parser = ioapi.ulsFileParser(path)
	elif path.endswith('.zip'):
		parser = ioapi.ulsZipParser(path)
	else:
		parser = ioapi.ulsFolderParser(path)

	for p in parser.parseMap:
		print "Parsing:",p
		for x in parser.parse(p):
			pp.pprint(x)
