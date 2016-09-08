#!/usr/bin/python

import sys

#input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    line = line.strip()
    result = line.split(",")
    print '%s\t%s' % (result[0], line)


