from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext


if __name__ == "__main__":

    #Create SparkContext
    sc = SparkContext(appName="PythonCrossProduct")

    #Read first file: course data
    courseData = sc.textFile(sys.argv[1], 1)

    #Read second file: professor data
    profData = sc.textFile(sys.argv[2], 1)

    #Write the code below to create an RDD that stores the cross product of the two tables and write the output

    courseProfCrossData = courseData.cartesian(profData)


    output = courseProfCrossData.collect()
    for course, prof in output:
        print("{},{}".format(course, prof))

    #Stop Spark
    sc.stop()
