#!/bin/python

"""
    reduce.py Get data from yellow and green NYC Taxis where key is the borough
    1 - Translate pickup latitude longitude to zip code
    2 - Include new columns:
      23: Dropoff borough
      24: Dropoff zip code
"""

import sys
import json
from shapely.geometry import shape, Point, Polygon

max_size = 200000000

z_file = open('zipcode_polygons.json', 'r')
z_string = z_file.read(max_size)
zipcode_json = json.loads(z_string)
z_file.close()

nyc_polygons = {}

all_zips = []
for zip_area in zipcode_json['features']:
  poly = shape(zip_area['geometry'])
  zip_code = zip_area['properties']['postalCode']
  all_zips.append(zip_code)
  borough = zip_area['properties']['borough']
  if borough not in nyc_polygons:
    nyc_polygons[borough] = {}

  if zip_code not in nyc_polygons[borough]:
    nyc_polygons[borough][zip_code] = [poly]
  else:
    nyc_polygons[borough][zip_code].append(poly)

for line in sys.stdin:
  key, value = line.replace('\r', '').replace('\n', '').split('\t')
  splitted = value.split(',')
  latitude, longitude = float(splitted[0]), float(splitted[1])

  all_attrs = splitted[2:]
  all_attrs_str = ','.join(all_attrs)

  if key == 'None':
    print "{0:s},{1:s},{2:s}".format(all_attrs_str, 'None', 'None')
    continue

  correct = False
  coordinate = Point(longitude, latitude)

  for zip_code in nyc_polygons[key]:
    for poly in nyc_polygons[key][zip_code]:
      correct = poly.contains(coordinate)
      if correct:
        print "{0:s},{1:.9f},{2:.9f},{3:s},{4:s}".format(all_attrs_str, latitude, longitude, key, zip_code)
        break
    else:
      continue
    break

  if not correct:
    print "{0:s},{1:.9f},{2:.9f},{3:s},{4:s}".format(all_attrs_str, latitude, longitude, key, 'None')
