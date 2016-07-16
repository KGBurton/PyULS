import sys
prev_line = ""
for line in sys.stdin:
	line = line.rstrip('\n')
	if len(line) > 2 and line[2] == "|":
		if( prev_line != "" ):
			sys.stdout.write(prev_line+"\n")
		prev_line = line
	else:
		prev_line += line
sys.stdout.write(prev_line+"\n")
