from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":
    
    #Create SparkContext 
    sc = SparkContext(appName="PythonCrossProduct")
    
    #Read first file: course data
    #tripsData = sc.textFile("aa")
    tripsData = sc.textFile(sys.argv[1], 1)
    tripsData = tripsData.map( lambda x: x.split(",") )
    tripsData = tripsData.filter( lambda x: len(x)>=15 )

    #Read second file: professor data
    #demogData = sc.textFile("merged_income_pop.csv")
    demogData = sc.textFile(sys.argv[2], 1)

    #filter to data
    demogData_f = demogData.map(lambda x: x.split(",")).filter(lambda x: len(x[2])>=1 )
    #demogData_f.count()

    # Split by comma (take the datetime as key and all the line as value)
    
    trip_values = tripsData.map(lambda x: (x[15], x[1] +","+ x[0] +","+ ",".join( x[2:]) ))
    demog_values = demogData_f.map(lambda x: (x[0], ",".join(x[1:]) ) )
    
    # Left Join
    dataset = trip_values.leftOuterJoin(demog_values)
    dataset_f = dataset.filter(lambda x: x[1][1] != None)
    data_output = dataset_f.map( lambda x: ( [i for i in x[1]][0]+","+[i for i in x[1]][1] ).encode('utf 8') ) 

    data_output_f = data_output.map(lambda x: x.split(",") )
    data_output_f = data_output_f.map(lambda x: x[0]+","+x[4]+","+x[14]+","+x[16]+","+x[19]+","+x[21]+","+x[22]+","+x[24]+","+x[25]+","+x[26]+","+x[27]+","+x[28]+","+x[29]+","+x[30]+","+x[31]+","+x[32]+","+x[33])

    output = data_output_f.coalesce(1).saveAsTextFile(sys.argv[1]+"_demog")

    sc.stop()
