#!/usr/bin/python

"""
    reduce.py Task 4-a reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None
total_trips = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
    revenue, tip_perc = value.split(',', 1)

    if key == current_key:
      total_trips += 1
      total_revenue += float(revenue)
      total_tip_perc += float(tip_perc)
    else:
        if current_key:
            avg_tip_perc = total_tip_perc / total_trips
            print "{0:s}\t{1:d},{2:.2f},{3:.2f}".format(current_key, total_trips, total_revenue, avg_tip_perc)
        total_trips = 1
        total_revenue = float(revenue)
        total_tip_perc = float(tip_perc)
        current_key = key

if total_trips:
  avg_tip_perc = total_tip_perc / total_trips
  print "{0:s}\t{1:d},{2:.2f},{3:.2f}".format(current_key, total_trips, total_revenue, avg_tip_perc)
