#!/usr/bin/python

"""
    map.py Task 2-d map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  key_cols = key.split(',')
  cols = value.split(',')

  day = key_cols[3].split()[0]

  total_revenue = float(cols[11]) + float(cols[12]) + float(cols[14])
  tolls_amount = float(cols[15])

  print "{0:s}\t{1:.2f}, {2:.2f}".format(day, total_revenue, tolls_amount)
