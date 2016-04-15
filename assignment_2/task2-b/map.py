#!/usr/bin/python

"""
    map.py Task 2-b map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  cols = value.split(',')

  total_amount = float(cols[16])
  if total_amount <= 10:
    print "{0:s}\t{1:d}".format('0,10', 1)
