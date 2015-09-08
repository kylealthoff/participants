import pandas as pd
import numpy as np
import math
from datetime import datetime
import sys

def generate_files(person, speed_of_person):
	participant = person
	speed = speed_of_person
	fileName = participant + '-Actigraph-' + speed + '-ms'

	df = pd.read_csv(fileName + '.csv', header=0)

	lengthList = []

	print df.dtypes

	date_object = datetime.strptime(df['Timestamp'][0], '%m/%d/%Y %I:%M:%S.%f')

	start_time = date_object
	print date_object

	times = []

	for i, row in df.iterrows():
		date_row = datetime.strptime(row['Timestamp'], '%m/%d/%Y %I:%M:%S.%f')
		new_time = date_row - start_time
		print new_time
		times.append(new_time)
		# removed X axis from summation function
		length = math.sqrt( (row['Axis1'] * row['Axis1']) + (row['Axis3'] * row['Axis3']))  
		lengthList.append(length)

	# LOW PASS FILTER 

	ALPHA = 0.1
	filteredList = []

	filteredList.append(lengthList[0])

	for i in range(len(lengthList)):
		if i != 0:
			filteredVal = ALPHA * lengthList[i] + ( 1 - ALPHA ) * filteredList[i - 1]
			filteredList.append(filteredVal)




	df['SUM'] = lengthList
	df['FILTER'] = filteredList
	df['Timestamp'] = times

	df.to_csv(fileName + '-sum.csv')

	df = df[ df.index >= 6000]
	df = df[ df.index <= 9005]

	df[['Axis1', 'Axis3', 'Timestamp']].to_json(participant + '-Actigraph-' + speed + '-sum.json')

	print df.dtypes

	mean = np.mean(lengthList)
	print mean

	print len(lengthList)
