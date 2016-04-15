#!/usr/bin/python

"""
    reduce.py Task 1 reduce
    Author: Ma. Elena Villalobos Ponte
"""

import sys

current_key = None
trips = []
fares = []


def print_joined(key, trips, fares):
    for trip in trips:
        for fare in fares:
            print "{0:s}\t{1:s},{2:s}".format(key, trip, fare)

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    key, value = line.strip().split('\t', 1)
    table_id, tuple_value = value.split(',', 1)

    if key == current_key:
        if table_id == 'T':
            trips.append(tuple_value)
        else:
            fares.append(tuple_value)
    else:
        if current_key:
            print_joined(current_key, trips, fares)
        trips = [tuple_value] if table_id == 'T' else []
        fares = [tuple_value] if table_id == 'F' else []
        current_key = key

if len(trips) > 0 and len(fares) > 0:
    print_joined(current_key, trips, fares)
