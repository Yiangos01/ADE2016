import sys
import csv
import math

#NW
Districts=[
["Hillington",51.5816,-0.4472],["Hillington",51.4984,-0.4304],["Hillington",51.5219,-0.4582],["Harrow",51.6008,-0.3284],["Harrow",51.5718,-0.3291],["Ealing",51.5152,-0.2959],["Ealing",51.5116,-0.3591],["Ealing",51.5398,-0.3643],["Hounslow",51.4512,-0.4129],["Hounslow",51.4844,-0.3237],["Hounslow",51.4741,-0.3758],["Brent",51.5761,-0.2776],["Brent",51.5556,-0.2913],["Brent",51.3477,-0.2367],["Barnet",51.5947,-0.2018],["Barnet",51.6298,-0.2416],["Barnet",51.6269,-0.1776],["Richmond",51.4279,-0.2018],["Richmond",51.4696,-0.2876],["Hammersmith & Fulham",51.5195,-0.2371],["Hammersmith & Fulham",51.4972,-0.2270],["Hammersmith & Fulham",51.4760,-0.2054],["Kesington",51.5015,-0.2039],["Kesington",51.5048,-0.1962],["Kesington",51.4896,-0.1886],["Westminster",51.5286,-0.1805],["Westminster",51.5141,-0.1617],["Westminster",51.5013,-0.1373],["Camden",51.5515,-0.1867],["Camden",51.5596,-0.1575],["Camden",51.5370,-0.1395],["Camden",51.5209,-0.1225],["Islington",51.5639,-0.1235],["Islington",51.5461,-0.1032],["Islington",51.5273,-0.0744],["City of London",51.5195,-0.1028],["City of London",51.5132,-0.0861],["Hackney",51.5652,-0.1028],["Hackney",51.5512,-0.0435],["Hackney",51.5369,-0.0744],["Haringey",51.5857,-0.1412],["Haringey",51.5967,-0.1218],["Haringey",51.5967,-0.0763],["Haringey",51.5844,-0.0917],["Enfield",51.6117,-0.1096],["Enfield",51.6184,-0.0722],["Enfield",51.6469,-0.1166],["Enfield",51.6332,-0.0468],["Enfield",51.6607,-0.0440],["Waltham Forest",51.6240,-0.0035],["Waltham Forest",51.5847,-0.0172],["Tower Hamlet",51.4983,-0.0167],["Tower Hamlet",51.5193,-0.0219],["Tower Hamlet",51.5279,-0.0416],["Tower Hamlet",51.5145,-0.0572],["Red Bridge",51.6067,0.0454],["Red Bridge",51.5969,0.1079],["Red Bridge",51.5704,0.0820],["Red Bridge",51.5745,0.0416],["Newham",51.5407,0.0007],["Newham",51.5197,0.0205],["Newham",51.5163,0.0692],["Newham",51.5456,0.0412],["Barking & Dagenham",51.5372,0.1157],["Barking & Dagenham",51.5564,0.1473],["Barking & Dagenham",51.5286,0.1473],["Havering",51.5231,0.1955],["Havering",51.5466,0.2292],["Havering",51.5991,0.1996],["Havering",51.5504,0.1285],["Bexley",51.4990,0.1369],["Bexley",51.4673,0.1767],["Bexley",51.4297,0.1180],["Bexley",51.4571,0.1135],["Grenwich",51.4895,0.0945],["Grenwich",51.4523,0.0540],["Grenwich",51.4823,0.0275],["Lewisham",51.4383,-0.0108],["Lewisham",51.4651,-0.0214],["Lewisham",51.4373,-0.0275],["Southwark",51.4365,-0.0848],["Southwark",51.4982,-0.0498],["Southwark",51.4755,-0.0769],["Southwark",51.4497,-0.0784],["Lambeth",51.4995,-0.1147],["Lambeth",51.4644,-0.1212],["Lambeth",51.4375,-0.1164],["Bromley",51.4071,-0.0454],["Bromley",51.4693,-0.0296],["Bromley",51.4260,-0.0483],["Bromley",51.4085,-0.0963],["Bromley",51.3556,-0.0106],["Sutton",51.4081,-0.2703],["Sutton",51.4227,-0.2171],["Sutton",51.3745,-0.2816],["Merton",51.4231,-0.2304],["Merton",51.3960,-0.2173],["Merton",51.4088,-0.1680],["Croydon",51.3880,-0.0962],["Croydon",51.3352,-0.0372],["Croydon",51.3018,-0.1084],["Wandsworth",51.4381,-0.1673],["Wandsworth",51.4693,-0.1645],["Wandsworth",51.4543,-0.2250],["Kingston",51.4156,-0.2590],["Kingston",51.3722,-0.2402],["Kingston",51.4000,-0.2402],["Kingston",51.3593,-0.2708]
]
#################################################

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
    		longi=float(words[5][:6])
    		lati=float(words[4][:6])
		for row in Districts:
			dist= float(math.sqrt(math.pow((float(row[1])-lati),2)+math.pow((float(row[2])-longi),2)))
			if bestdist > dist :
				loc=row[0];
				bestdist=dist
		print(loc+"\t1")
		print(str(lati)+","+str(longi))
		bestdist=1000
			



