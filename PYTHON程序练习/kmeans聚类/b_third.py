import matplotlib
import matplotlib.pyplot as plt
from numpy import *

dataMat_A = []
dataMat_B = []
dataMat_C = []
dataMat_D = []
dataMat_all = []
dataList_final = []

def get_geo_dict(filename):
    global dataMat_all
    global dataList_final
    
    file_result = open(filename,"r")
    allline = file_result.readlines()
    geo_dict = {}
    for eachline in allline:
        line = eachline[0:(len(eachline)-1)]
        line_con = line.split(" ")
        geo_dict[line_con[0]] = []
        geo_dict[line_con[0]].append(int(line_con[1]))
        geo_dict[line_con[0]].append(int(line_con[2]))

    dataList = []
    for item in geo_dict.keys():
        dataList.append(geo_dict[item])
    dataMat = mat(dataList)
    dataList_final.extend(dataList)

    return dataMat

def vec_in_Mat(vec,mat):
    if (vec[:,0] <= max(mat[:,0]) and vec[:,0]>= min(mat[:,0])) and( vec[:,1] <= max(mat[:,1]) and vec[:,1]>= min(mat[:,1])):
        return True
        

def distance(vecA,vecB):
    if vec_in_Mat(vecA,dataMat_A) and vec_in_Mat(vecB,dataMat_A):
        return sqrt(sum(power(vecA-vecB,2)))
    elif vec_in_Mat(vecA,dataMat_B) and vec_in_Mat(vecB,dataMat_B):
        return sqrt(sum(power(vecA-vecB,2)))
    elif vec_in_Mat(vecA,dataMat_C) and vec_in_Mat(vecB,dataMat_C):
        return sqrt(sum(power(vecA-vecB,2)))
    elif vec_in_Mat(vecA,dataMat_D) and vec_in_Mat(vecB,dataMat_D):
        return sqrt(sum(power(vecA-vecB,2)))
    else:
        return float(sqrt(sum(power(vecA-vecB,2))) + 10000.0)

def randCent(dataset,k):
    n = shape(dataset)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minj = min(dataset[:,j])
        print minj
        rangej = float(max(dataset[:,j]) - minj)
        print rangej
        centroids[:,j] = minj+rangej*random.rand(k,1)
    return centroids



def kMeans(dataset,k,distMeas = distance,createcent = randCent):
    m = shape(dataset)[0]
    clusterAssmet = mat(zeros((m,2)))
    centroids = createcent(dataset,k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;minIndex = -1
            for j in range(k):
                distji = distMeas(centroids[j,:],dataset[i,:])
                if distji < minDist:
                    minDist = distji;minIndex = j
            if clusterAssmet[i,0] != minIndex:clusterChanged = True
            clusterAssmet[i,:] = minIndex,minDist**2
        for cent in range(k):
            pointClust = dataset[nonzero(clusterAssmet[:,0].A == cent)[0]]
            centroids[cent,:] = mean(pointClust,axis = 0)
    return centroids,clusterAssmet

if __name__ == '__main__':
    
    filename = "A.txt"
    dataMat_A = get_geo_dict(filename)
    print dataMat_A

    filename = "B.txt"
    dataMat_B = get_geo_dict(filename)

    filename = "C.txt"
    dataMat_C = get_geo_dict(filename)

    filename = "D.txt"
    dataMat_D = get_geo_dict(filename)

    dataMat_all = mat(dataList_final)

    print len(dataMat_A)

    '''
    for i in dataMat_all:
        for j in dataMat_A:
            if (i == j).all():
                print i
                print "yes"
                
    '''
    
    print randCent(dataMat_A,3)
    
    myCentroid,clustAssig = kMeans(dataMat_all,4)
    #print clustAssig
    fig = plt.figure()
    rect = [0.1,0.1,0.8,0.8]
    axprops = dict(xticks = [],yticks = [])
    ax0 = fig.add_axes(rect,label = 'ax0',**axprops)
    imgP = plt.imread('addr2.png')
    ax0.imshow(imgP)

    #plt.xlim(0.0,12.0)
    #plt.ylim(0.0,12.0)

    scatterMarkers = ['s','o','^','8','p','d','v','h','>','<']
    color_set = ["yellow","red","blue","green"]

    axprops = dict(xticks = [],yticks = [])
    ax1 = fig.add_axes(rect,label = 'ax1',frameon = False)
    for i in range(4):
        pointinClust = dataMat_all[nonzero(clustAssig[:,0].A == i)[0],:]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        color_draw = color_set[i%len(color_set)]
        ax1.scatter(pointinClust[:,0].flatten().A[0],pointinClust[:,1].flatten().A[0],marker = markerStyle,color = color_draw, s=90)

    ax1.scatter(myCentroid[:,0].flatten().A[0],myCentroid[:,1].flatten().A[0],marker='+',color = "purple",s=300)
    plt.show()
    #Draw_pic(geo_dict)
