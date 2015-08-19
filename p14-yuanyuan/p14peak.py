import pandas as pd
import numpy as np
import math
from peakdet import peakdet

df = pd.read_csv('P14-Actigraph-0_9-ms-v2.csv', header=0)

ymax, ymin = peakdet(df['Axis2'], .1)
zmax, zmin = peakdet(df['Axis3'], .1)


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