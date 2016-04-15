#!/usr/bin/python

"""
    reduce.py Task 2-a reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys
import string

current_key = None
count = None

ranges = ["0,4"]
ranges += ["{0:.2f},{1:.0f}".format(i + (0.01 * (i > 0)), i + 4) for i in range(4, 48, 4)]
ranges.append("48.01,infinite")

alphabet = string.ascii_lowercase

ranges_match = {}

for i, str_range in enumerate(ranges):
    ranges_match[alphabet[i]] = str_range

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.strip().split('\t', 1)

    if key == current_key:
      count += int(value)
    else:
        if current_key:
            print "{0:s}\t{1:d}".format(ranges_match[current_key], count)
        count = int(value)
        current_key = key

if count:
    print "{0:s}\t{1:d}".format(ranges_match[current_key], count)
