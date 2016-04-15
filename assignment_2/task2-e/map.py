#!/usr/bin/python

"""
    map.py Task 2-e map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  key_cols = key.split(',')
  cols = value.split(',')

  day = key_cols[3].split()[0]
  medallion = key_cols[0]

  print "{0:s}\t{1:s}".format(medallion, day)
