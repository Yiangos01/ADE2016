import sys
import csv
import math

data = sys.stdin.readlines()
csvreader = csv.reader(data)

for row in csvreader:
	tweet = row[0].split("\t")
	text = tweet[2].split(" ")
	for word in text:
		print(word+"\t1")

