from __future__ import print_function

import sys

from pyspark import SparkContext

def create_trip_pair(trip):
    features = trip.strip().split(',')
    key = features[13]
    # Swap 0 and 1 values
    features[0], features[1] = features[1], features[0]
    values = ",".join(features)
    return (key, values)

def create_demog_pair(demog):
    features = demog.strip().split(",", 1)
    return tuple(features)

if __name__ == "__main__":

    # Create SparkContext
    sc = SparkContext(appName="DatasetJoin")

    # Read first file: trips data
    tripsData = sc.textFile(sys.argv[1])

    # Read second file: demographic data
    demogData = sc.textFile(sys.argv[2])

    # Split by comma (take the datetime as key and all the line as value)
    trip_values = tripsData.map(create_trip_pair)
    demog_values = demogData.map(create_demog_pair)

    # Left Join
    joined = trip_values.join(demog_values)
    joined_csv = joined.map(lambda res: str(res[1][0]) + ',' + str(res[1][1]))
    output = joined_csv.saveAsTextFile(sys.argv[3])
    sc.stop()
