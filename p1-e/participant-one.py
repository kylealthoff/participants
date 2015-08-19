import pandas as pd
import numpy as np
import math

df = pd.read_csv('P01-Androsensor-0_9-start-stop.csv', header=0)

lengthList = []

print df.dtypes

xLabel = 'LINEAR ACCELERATION X'
yLabel = 'LINEAR ACCELERATION Y'
zLabel = 'LINEAR ACCELERATION Z'

for i, row in df.iterrows():
	length = math.sqrt( (row[xLabel] * row[xLabel]) + (row[yLabel] * row[yLabel]) + (row[zLabel] * row[zLabel]))  
	lengthList.append(length)


# LOW PASS FILTER 

ALPHA = 0.1
filteredList = []

filteredList.append(lengthList[0])
print filteredList

for i in range(len(lengthList)):
	print i
	if i != 0:
		filteredVal = ALPHA * lengthList[i] + ( 1 - ALPHA ) * filteredList[i - 1]
		filteredList.append(filteredVal)


df['SUM'] = lengthList
df['FILTER'] = filteredList

df.to_csv('P01-Androsensor-0_9-start-stop-sum-filter.csv')

print df.dtypes

mean = np.mean(lengthList)
print mean

print len(lengthList)







