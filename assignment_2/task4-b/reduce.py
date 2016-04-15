#!/usr/bin/python

"""
    reduce.py Task 4-b reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys
import bisect


def set_top(top_n, agent_name, total_revenue, n=20):
  sorted_keys = [i[0] for i in top_n if i != None]
  index = bisect.bisect_left(sorted_keys, total_revenue)
  if (index >= 0 and index < n):
    top_n = top_n[:index] + [(total_revenue, agent_name)] + top_n[index:]
  elif index == n:
    top_n.append((total_revenue, agent_name))
  if len(top_n) > n and top_n[-1] != None:
    top_n = top_n[-n:]
  elif len(top_n) > n and top_n[-1] == None:
    top_n = top_n[:n]
  return top_n

current_key = None
current_agent_name = None
n = 20
top_n = [None] * n

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t', 1)
  splitted = value.split('"')
  agent_name = splitted[1]
  revenue = splitted[2].split(',')[1]

  if key == current_key:
    total_revenue += float(revenue)
  else:
    if current_key:
      top_n = set_top(top_n, current_agent_name, total_revenue)
    total_revenue = float(revenue)
    current_key = key
    current_agent_name = agent_name

top_n = set_top(top_n, agent_name, total_revenue)

# Remove None values from top
if None in top_n:
  top_n[:] = [x for x in top_n if x != None]

top_n.sort(key=lambda elem: elem[0], reverse=True)

for (total_revenue, agent_name) in top_n:
  print "{0:s}\t{1:.2f}".format(agent_name, total_revenue)
