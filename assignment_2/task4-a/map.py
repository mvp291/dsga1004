#!/usr/bin/python

"""
    map.py Task 4-a map
    Author: Ma. Elena Villalobos Ponte
"""

import sys
import StringIO
import csv

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').replace('\t', ',').split(',', 1)
  csv_file = StringIO.StringIO(value)
  csv_reader = csv.reader(csv_file)
  for record in csv_reader:
    # Column number
    # 14 - fare_amount
    # 17 - tip_amount
    # 15 - surcharge
    # 25 - vehicle_type
    total_revenue = float(record[14]) + float(record[17]) + float(record[15])
    tip_percentage = 100 * (float(record[17]) / total_revenue) if total_revenue else 0

    print "{0:s}\t{1:f}, {2:f}".format(record[25], total_revenue, tip_percentage)
