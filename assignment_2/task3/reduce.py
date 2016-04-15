#!/usr/bin/python

"""
    reduce.py Task 3 reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None
trips_fares = []
vehicles = []


def print_joined(key, t1, t2):
    for elem_i in t1:
        for elem_j in t2:
            print "{0:s}\t{1:s},{2:s}".format(key, elem_i, elem_j)

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.strip().split('\t', 1)
    table_id, tuple_value = value.split(',', 1)

    if key == current_key:
        if table_id == 'TF':
            trips_fares.append(tuple_value)
        else:
            vehicles.append(tuple_value)
    else:
        if current_key:
            print_joined(current_key, trips_fares, vehicles)
        trips_fares = [tuple_value] if table_id == 'TF' else []
        vehicles = [tuple_value] if table_id == 'V' else []
        current_key = key

if len(trips_fares) > 0 and len(vehicles) > 0:
    print_joined(current_key, trips_fares, vehicles)
