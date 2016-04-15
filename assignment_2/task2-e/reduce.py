#!/usr/bin/python

"""
    reduce.py Task 2-e reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, day = line.replace('\r', '').replace('\n', '').split('\t', 1)

    if key == current_key:
      total_trips += 1
      if day not in total_per_day.keys():
        total_per_day[day] = 0
      total_per_day[day] += 1
    else:
        if current_key:
            avg_per_day = sum(total_per_day.values()) / float(len(total_per_day))
            print "{0:s}\t{1:d},{2:.2f}".format(current_key, total_trips, avg_per_day)
        total_trips = 1
        total_per_day = {}
        total_per_day[day] = 1
        current_key = key

avg_per_day = sum(total_per_day.values()) / float(len(total_per_day))
print "{0:s}\t{1:d},{2:.2f}".format(current_key, total_trips, avg_per_day)
