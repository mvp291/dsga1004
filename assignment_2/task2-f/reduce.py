#!/usr/bin/python

"""
    map.py Task 2-f reduce
    Author: Ma. Elena Villalobos Ponte
"""
import sys

current_key = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)

    if key == current_key:
        if value not in medallions:
            medallions.append(value)
    else:
        if current_key:
            print "{0:s}\t{1:d}".format(current_key, len(medallions))
        medallions = [value]
        current_key = key

print "{0:s}\t{1:d}".format(current_key, len(medallions))
