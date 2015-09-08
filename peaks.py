import pandas as pd
import numpy as np
import math
from peakdet import peakdet

def getAverages(person, speed_of_person):
	participant = person
	speed = speed_of_person
	df = pd.read_csv(participant + '-Actigraph-' + speed + '-ms-sum.csv', header=0)

	yAxis = df['Axis1']
	zAxis = df['Axis3']

	print 'Speed: ' + speed

	print 'Z length: ' + str(len(zAxis))

	print 'Y length: ' + str(len(yAxis))

	zsum = 0
	for item in zAxis:
		zsum += (item ** 2) 

	zavg = math.sqrt(zsum) / len(zAxis)

	print 'Z Avg: ' + str(zavg) 

	ysum = 0

	for item in yAxis:
		 ysum += (item ** 2)

	yavg = math.sqrt(ysum) / len(yAxis)

	print 'Y Avg: ' + str(yavg)
