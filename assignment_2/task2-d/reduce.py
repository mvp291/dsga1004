#!/usr/bin/python

"""
    map.py Task 2-d reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.strip().split('\t', 1)
    revenue, tolls = value.split(',')

    if key == current_key:
      total_revenue += float(revenue)
      total_tolls += float(tolls)
    else:
        if current_key:
            print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_revenue, total_tolls)
        total_revenue = float(revenue)
        total_tolls = float(tolls)
        current_key = key

print "{0:s}\t{1:.2f},{2:.2f}".format(current_key, total_revenue, total_tolls)
