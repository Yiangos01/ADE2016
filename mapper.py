import sys
import csv
#mape=open("mapperout.txt",'w')
#input comes from STDIN (standard 
data = sys.stdin.readlines()
csvreader = csv.reader(data, delimiter=',')
for row in csvreader:
	words=row[0].split("\t")
	if len(words) > 6 :
		print (words[0]+","+words[4]+","+words[5])	
    
