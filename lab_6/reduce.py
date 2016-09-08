#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
prof = []
courses = []
for line in sys.stdin:
	line = line.split(',')
	if line[0].startswith("1"):
		prof.append(line[1] + ", " + line[2].strip())
	elif line[0].startswith("2"):
		courses.append(line[1] + ", " + line[2].strip())

for c in courses:
	for p in prof:
		print p +", "+ c