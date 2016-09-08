#!/bin/python

"""
    map.py Get raw data from yellow and green NYC Taxis and
    1 - Translate pickup latitude longitude to borough
    2 - Sort green taxi data columns to match yellow taxi data
    3 - Eliminate unnecessary columns
    4 - Include indicator of source
      Y: yellow taxi data
      G: green taxi data
"""

import sys
import json
import datetime
from pytz import timezone
from shapely.geometry import shape, Point, Polygon

def str_to_datetime(str_dt):
  unaware_est = datetime.datetime.strptime(str_dt,"%Y-%m-%d %H:%M:%S")
  localtz = timezone('US/Eastern')
  aware_est = localtz.localize(unaware_est)
  return aware_est

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
lat_ix = 5
long_ix = 6
for line in sys.stdin:
  clean_line = line.replace('\r', '').replace('\n', '')
  splitted = clean_line.split(',')

  try:
    longitude, latitude = float(splitted[lat_ix]), float(splitted[long_ix])
  except (TypeError, ValueError): # header line, ignore it
    continue

  if len(splitted) == 19: # yellow taxi data
    # Only include relevant columns
    col_order = [1, 2, 3, 4, 7, 9, 10, 11, 12, 13, 15, 18]
    color = 'Y'
  else: # green taxi data
    # all data column order [0, 1, 2, 9, 10, 5, 6, 4, 3, 7, 8, 19, 11, 12, 13, 17, 14, 15, 18]
    col_order = [1, 2, 9, 10, 4, 7, 8, 19, 11, 12, 17, 18]
    color = 'G'

  original_data = [splitted[i] for i in col_order]
  output_data = ','.join(original_data)

  # Eliminate ouliers for trip distance
  try:
    trip_distance = float(original_data[3])
    if trip_distance < 0 or trip_distance > 100:
      continue
  except (TypeError, ValueError):
    continue

  # Eliminate ouliers for trip fare amount
  try:
    total_amount = float(original_data[10])
    if total_amount < 0 or total_amount > 500:
      continue
  except (TypeError, ValueError):
    continue

  # Create trip length feature
  try:
    time_delta = str_to_datetime(original_data[1]) - str_to_datetime(original_data[0])
    trip_length = round(time_delta.seconds / float(60), 2)
  except:
    trip_length = None


  for i in borough_ids:
    coordinate = Point(longitude, latitude)
    correct = borough_polygons[i]['polygon'].contains(coordinate)
    if correct:
      print "{0:s}\t{1:.9f},{2:.9f},{3:.2f},{4:s},{5:s}".format(borough_polygons[i]['name'], latitude, longitude, trip_length, output_data, color)
      break

  if not correct:
    print "{0:s}\t{1:.9f},{2:.9f},{3:.2f},{4:s},{5:s}".format('None', latitude, longitude, trip_length, output_data, color)

