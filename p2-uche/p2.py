import pandas as pd
import numpy as np
import math

speed = '0_9'
fileName = 'P02-Actigraph-' + speed + '-ms-v2'

df = pd.read_csv(fileName + '.csv', header=0)

lengthList = []

print df.dtypes

startTime = df['Timestamp'][0]
print startTime

times = []

for i, row in df.iterrows():
	newTime = row['Timestamp'] - startTime
	newTime = round(newTime, 1)
	times.append(newTime)
	length = math.sqrt( (row['Axis1'] * row['Axis1']) + (row['Axis2'] * row['Axis2']) + (row['Axis3'] * row['Axis3']))  
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

df[['SUM', 'Timestamp']].to_json('P02-Actigraph-' + speed + '-sum.json')

print df.dtypes

mean = np.mean(lengthList)
print mean

print len(lengthList)







