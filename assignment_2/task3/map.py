#!/usr/bin/python

"""
    map.py Task 3 map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').replace('\t', ',').split(',', 1)
  raw_cols = value.split(',')
  last_col = value.split(',')[-1]
  if raw_cols[0] == 'medallion':
    continue
  else:
    try:
      float(last_col)
      table_id = 'TF'
    except:
      table_id = 'V'

    print "{0:s}\t{1:s},{2:s}".format(key, table_id, value)
