import sys
import csv
import math

#NW

#################################################
csv.field_size_limit(sys.maxsize)

def condot(str):
	for c in str:
		if (c=='.') :
			return 1
	return 0

dist= 1000
bestdist= 1000
loc="a"
x=1
y=1
data = sys.stdin.readlines()
csvreader = csv.reader(data, delimiter=',')
for row in csvreader:
	words=row[0].split("\t")
	if len(words) > 6 :
		if (condot(words[5]) and condot(words[4])):
    			longi=float(words[5][:5])
			lati=float(words[4][:5])			
			if (longi>0 and lati>0) :
				print(words[5][:4]+words[4][:4]+"\t1")
			elif (longi<0 and lati>0) :
				print(words[5][:5]+words[4][:4]+"\t1")
			elif (longi>0 and lati<0) :
				print(words[5][:4]+words[4][:5]+"\t1")
			elif (longi<0 and lati<0) :
				print(words[5][:5]+words[4][:5]+"\t1")
		#else :
			#print ("wrong line\n")
		bestdist=1000
			



