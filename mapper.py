import sys
import csv
import math

#NW
NW=[
["Hilingdon",51.5346,-0.4543],["Hounson",51.4620,-0.3720],["Ealing",51.5124,-0.3051],["Harrow",51.5798,-0.3418],["Bret",51.5506,-0.2556],["Barnet",51.6570,-0.1943],["Westminster",51.4971,-0.1353],["Belgravia",51.4973,-0.153],["Chealsea",51.4845,-0.1754],["Fulham",51.4760,-0.1992],["Camden",51.5384,-0.1430],["Isington",51.5386,-0.1051],["Harringey",51.5801,-0.1027],["Enfield",51.6495,-0.0800],["Hachey",51.5436,-0.0545],["CityofLondon",51.5096,-0.0922],["Marrylobone",51.5194,-0.15874],["Mayfair",51.5001,-0.1472] ,["SOHO",51.5134,-0.1346],["Kings Cross",51.5302,-0.1259],["Kensington",51.4972,-0.1901],["Fitzrovia",51.5205,-0.1366]
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
		if longi < -0.07 :
			if lati > 51.48 :
				#print("NorthWest\t"+"1")
				for row in NW:
					dist= float(math.sqrt(math.pow((float(row[1])-lati),2)+math.pow((float(row[2])-longi),2)))
					if bestdist > dist :
						loc=row[0];
						bestdist=dist
				print(loc+"\t1")
				print(str(lati)+","+str(longi))
				bestdist=1000
			else:
				print("SouthWest\t"+"1")
		else:
			if lati > 51.48 :
				print("NorthEast\t"+"1")
			else:
		    		print("SouthEast\t"+"1")




