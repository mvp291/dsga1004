#!/usr/bin/python

"""
    reduce.py Task 2-b reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None
count = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.strip().split('\t', 1)

    if key == current_key:
      count += int(value)
    else:
        if current_key:
            print "{0:d}".format(count)
        count = int(value)
        current_key = key

if count:
    print "{0:d}".format(count)
