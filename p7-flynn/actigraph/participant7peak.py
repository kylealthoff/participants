import pandas as pd
import numpy as np
import math
from peakdet import peakdet

df = pd.read_csv('P07-Actigraph-0_9-ms-v2-start-stop-sum.csv', header=0)

maxtab, mintab = peakdet(df['FILTER'], .1)

ymax, ymin = peakdet(df['Axis2'], .1)
zmax, zmin = peakdet(df['Axis3'], .1)

print 'FILTER Max length: ' + str(len(maxtab))
print 'FILTER Min length: ' + str(len(mintab))

print 'Z max length: ' + str(len(zmax))
print 'Z min length: ' + str(len(zmin))

print 'Y max length: ' + str(len(ymax))
print 'Y min length: ' + str(len(ymin))

zsum = 0
for item in zmax:
	zsum += item[1]

zavg = zsum / len(zmax)

print 'Z Avg: ' + str(zavg)

ysum = 0

for item in ymax:
	 ysum += item[1]

yavg = ysum / len(ymax)

print 'Y Avg: ' + str(yavg)