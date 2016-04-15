#!/usr/bin/python

"""
    combine.py Task 2-c combine
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  cols = value.split(',')

  passenger_count = int(cols[3])
  print "{0:d}\t{1:d}".format(passenger_count, 1)
