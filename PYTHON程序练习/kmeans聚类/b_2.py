import matplotlib
import matplotlib.pyplot as plt
from numpy import *


file_result = open("geo.txt","r")

allline = file_result.readlines()

geo_dict = {}

for eachline in allline:
    line = eachline[0:(len(eachline)-1)]
    line_con = line.split(" ")
    geo_dict[line_con[0]] = []
    geo_dict[line_con[0]].append(int(line_con[1]))
    geo_dict[line_con[0]].append(int(line_con[2]))

print geo_dict

dataList = []

for item in geo_dict.keys():
    dataList.append(geo_dict[item])
    
dataMat = mat(dataList)
print dataMat

fig = plt.figure()
rect = [0,0,10,10]
scatterMarkers = ['s','o','^','8','p','d','v','h','>','<']
axprops = dict(xticks = [],yticks = [])
ax0 = fig.add_axes(rect,label = 'ax0',**axprops)

imgP = plt.imread('addr.png')
ax0.imshow(imgP)
ax1 = fig.add_axes(rect,label = 'ax1',frameon = False)

for i in range(0,1):
    point_real = dataMat[nonzero(dataMat[:,0].A == i)[0],:]
    print point_real[1,0].flatten().A[0]
    markerStyle = scatterMarkers[1]
    ax1.scatter(point_real[:,0].flatten().A[0],point_real[:,1].flatten().A[0],marker = markerStyle,s = 90)
plt.show()





    
