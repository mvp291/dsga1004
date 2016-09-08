from __future__ import print_function

import sys

from pyspark import SparkContext
import datetime
from pytz import timezone


def str_to_datetime(str_dt):
    unaware_est = datetime.datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S")
    localtz = timezone('US/Eastern')
    aware_est = localtz.localize(unaware_est)
    return aware_est


def generate_cols(trip):
    features = trip.strip().replace('\t', '').split(',')

    # Create trip length feature
    try:
        time_delta = str_to_datetime(features[2]) - str_to_datetime(features[1])
        trip_length = str(round(time_delta.seconds / float(60), 2))
    except:
        trip_length = 'None'

    features_order = [1, 2, 3, 4, 5, 6, 9, 10, 11, 13, 15, 18, 19, 20, 21, 22, 23]
    values = ','.join([trip_length] + [features[i] for i in features_order])
    return values


def outliers_filter(trip):
    features = trip.strip().split(",")
    trip_distance = float(features[4])
    total_amount = float(features[18])
    if trip_distance > 0 and trip_distance < 100:
        if total_amount > 0 and total_amount < 300:
            return True
    return False

if __name__ == "__main__":

    # Create SparkContext
    sc = SparkContext(appName="OutliersAndFilter")

    # Read first file: trips data
    tripsData = sc.textFile(sys.argv[1])
    filtered = tripsData.filter(outliers_filter)
    sorted_cols = filtered.map(generate_cols)
    num_parts = sorted_cols.coalesce(5)
    output = sorted_cols.saveAsTextFile(sys.argv[2])
    sc.stop()
