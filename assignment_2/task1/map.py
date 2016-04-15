#!/usr/bin/python

"""
    map.py Task 1 map
    Author: Ma. Elena Villalobos Ponte
"""

import sys

for line in sys.stdin:
  raw_cols = line.replace('\r', '').replace('\n', '').split(',')
  if raw_cols[0] == 'medallion':
    continue
  else:

    if len(raw_cols) == 14: # Trip tuple
      table_id = 'T'
      key_cols_pos = [0, 1, 2, 5]
    else:
      table_id = 'F'
      key_cols_pos = [0, 1, 2, 3]

    key = []
    value = []
    for pos in xrange(len(raw_cols)):
      if pos in key_cols_pos:
        key.append(raw_cols[pos])
      else:
        value.append(raw_cols[pos])

    str_key = ','.join(key)
    str_value = ','.join(value)
    print "{0:s}\t{1:s},{2:s}".format(str_key, table_id, str_value)
