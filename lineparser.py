#!/usr/bin/python
#I am not proud of thise code. It mashes mysql CSV format into sqlite dump format.
#However, I am 70% certain the FCC has a schizophrenic schema, as the number of columns sometimes changes.
import sys
import re

def output(line):
	sys.stdout.write(line.replace('"','\\"')+"\n")

prev_line = ""
for line in sys.stdin:
	line = line.rstrip('\n')
	if re.search( "^[a-zA-Z0-9][a-zA-Z0-9]\|", line ):
		if( prev_line != "" ):
			output(prev_line)
			prev_line = ""
		prev_line = line
	else:
		prev_line += line
output(prev_line)
