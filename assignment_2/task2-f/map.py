#!/usr/bin/python

"""
    map.py Task 2-f map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  key_cols = key.split(',')
  cols = value.split(',')

  medallion = key_cols[0]
  driver = key_cols[1]

  print "{0:s}\t{1:s}".format(driver, medallion)
