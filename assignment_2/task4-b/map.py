#!/usr/bin/python

"""
    map.py Task 4-b map
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
    # 28 - agent_number
    # 29 - agent_name

    agent_number = record[28]
    agent_name = record[29]
    total_revenue = float(record[14]) + float(record[17]) + float(record[15])

    print '{0:s}\t"{1:s}", {2:.2f}'.format(agent_number, agent_name, total_revenue)
