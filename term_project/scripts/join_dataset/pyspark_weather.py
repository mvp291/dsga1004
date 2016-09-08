from __future__ import print_function

import sys
from operator import add
from datetime import timedelta
from pyspark import SparkContext


if __name__ == "__main__":
    
    #Create SparkContext 
    sc = SparkContext(appName="PythonCrossProduct")
    
    #Read first file: 
    tripsData = sc.textFile(sys.argv[1], 1)
    tripsData = tripsData.map( lambda x: x.split(",") )
    tripsData = tripsData.filter( lambda x: len(x)>=15 )

    #Read second file: 
    weatherData = sc.textFile(sys.argv[2], 1)

    #filter to data
    weatherData_f = weatherData.map(lambda x: x.split(",")).filter(lambda x: len(x[2])>=1 )

    # Split by comma (take the datetime as key and all the line as value)
    
    trip_values = tripsData.map(lambda x: (x[1].split(" ")[0], x[1].split(" ")[1]+","+ x[0] +","+ ",".join(x[2:]) ) )        
    weather_values = weatherData_f.map(lambda x: (x[0].split(" ")[0], x[0].split(" ")[1]+","+ ",".join(x[1:]) ) )
    
    # Left Join
    dataset = trip_values.leftOuterJoin(weather_values)
    dataset_f1 = dataset.filter(lambda x: x[1][1] != None)

    # Look for a weather (in an hour)

    def different_hours( tup ):
        hr1 = tup[1][0].split(",")[0]
        hr2 = tup[1][1].split(",")[0]
        hr_delt1 = timedelta(hours=int(hr1.split(":")[0]), minutes=int(hr1.split(":")[1]))
        hr_delt2 = timedelta(hours=int(hr2.split(":")[0]), minutes=int(hr2.split(":")[1]))
        diff =abs(hr_delt1 - hr_delt2)
        minutes = diff.seconds/60
        return ( (tup[0],tup[1]),minutes)

    dataset_f2 = dataset_f1.map(lambda x: different_hours(x) )
    dataset_f3 = dataset_f2.filter(lambda x: x[1] <= 60)
    dataset_reduced = dataset_f3.reduceByKey(lambda x,y: min(x,y))
    dataset_reduced_tup = dataset_reduced.map(lambda x: (x[0][0],x[0][1]) )

    data_output = dataset_reduced_tup.map( lambda x: ( [i for i in x[1]][0]+","+[i for i in x[1]][1] ).encode('utf 8') )  
    output = data_output.coalesce(1).saveAsTextFile(sys.argv[1]+"_demog")

    sc.stop()
