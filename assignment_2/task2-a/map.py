#!/usr/bin/python

"""
    map.py Task 2-a map
    Author: Ma. Elena Villalobos Ponte
"""

import sys
import string

alphabet = string.ascii_lowercase

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  cols = value.split(',')

  fare_amount = round(float(cols[11]), 2)

  ranges = [(i + (0.01 * (i > 0)), i + 4) for i in range(0, 48, 4)]
  ranges.append((48.01, None))

  for i, (inf, sup) in enumerate(ranges):
    if fare_amount >= inf and (fare_amount <= sup or not sup):
      print "{0:s}\t{1:d}".format(alphabet[i], 1)
      break
