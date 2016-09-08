from __future__ import print_function

import sys
from operator import add

from pyspark import SparkContext
from pyspark.mllib.fpm import FPGrowth


if __name__ == "__main__":
    sc = SparkContext(appName="FreqItems")
    data = sc.textFile(sys.argv[1])
    transactions = data.map(lambda line: line.strip().split(','))
    model = FPGrowth.train(transactions, minSupport=0.1, numPartitions=10)
    results = (model.freqItemsets()).collect()
    for line in results:
        print("%s" % (str(line)))

    sc.stop()
