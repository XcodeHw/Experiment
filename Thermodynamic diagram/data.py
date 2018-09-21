import pandas as pd
import json

den = pd.read_csv('IMG_4.csv', sep=',', header=None).as_matrix()
data=""
#print(den.shape[0])768
lat=30.752361
lng=103.933394
for i in range(1,den.shape[0]):
     lat=lat-0.0001
     lng=103.933394
     for j in range(1,den.shape[1]):
	 
        lng=lng+0.0001
        if den[i][j]>0.0000001:
            temp="{"+'"lat":'+str(lat)+',"lng":'+str(lng)+',"count":'+str(den[i][j])+"},"
            data=data+temp
data=data.rstrip(',')
data.replace('\\','')

data="var heatmapData=[" +data+"];"

filename = './json2.txt'
with open(filename,'a+') as f:
   f.write(data)
