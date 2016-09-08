import sys
import operator
import os

k = int(float(sys.argv[1]))
inputdir = str(sys.argv[2])
outputfile = str(sys.argv[3])
count={'None':0}

flo = open(outputfile,'w')

for inputfile in os.listdir(inputdir): 
	fl = open(inputdir+inputfile,'r')
	for line in fl:
		words=line.split()
		count[words[0]]= int(float(words[1]))
	fl.close()
	
for i in range(0,k):
	tpword = max(count.iteritems(), key=operator.itemgetter(1))[0]
       	flo.write("%s\t%s\n" %(tpword, count[tpword]))
       	count[tpword]=0

flo.close()

