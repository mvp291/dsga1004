#!/bin/python

"""
    map.py Get data from yellow and green NYC Taxis after processing pickup
    1 - Translate dropoff latitude longitude to borough
"""

import sys
import json
from shapely.geometry import shape, Point, Polygon

# Read borough polygons from file and create Shapely Polygons
max_size = 200000000

b_file = open('borough_polygons.json', 'r')
b_string = b_file.read(max_size)
borough_json = json.loads(b_string)
b_file.close()

borough_polygons = {}

correct = False
for borough in borough_json['features']:
  poly = shape(borough['geometry'])
  borough_name = borough['properties']['borough']
  borough_polygons[borough['id']] = {'name': borough_name, 'polygon': poly}

# Map each trip with the corresponding borough or none if there is no match

# Preferred order for borough polygon checking
# Manhattan, Queens, Brooklyn, Staten Island, Bronx
borough_ids = range(45, 74) + range(4, 24) + range(24, 44) + range(0, 4) + range(74, 104)

# Indexes of pickup latitude and longitude
lat_ix = 6
long_ix = 7
for line in sys.stdin:
  clean_line = line.replace('\r', '').replace('\n', '').replace('\t', '')
  splitted = clean_line.split(',')

  all_attr = ",".join(splitted[:6] + splitted[8:])

  try:
    longitude, latitude = float(splitted[lat_ix]), float(splitted[long_ix])
  except: # header line, ignore it
    continue

  for i in borough_ids:
    coordinate = Point(longitude, latitude)
    correct = borough_polygons[i]['polygon'].contains(coordinate)
    if correct:
      print "{0:s}\t{1:.9f},{2:.9f},{3:s}".format(borough_polygons[i]['name'], latitude, longitude, all_attr)
      break

  if not correct:
    print "{0:s}\t{1:.9f},{2:.9f},{3:s}".format('None', latitude, longitude, all_attr)

