#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## K-means算法
import numpy as np
import matplotlib.pyplot as plt


def initCenters(dataSet, k):
    numSamples, dim = dataSet.shape
    centers = np.zeros((k, dim))
    for i in range(k):
        # random get k centers
        index = int(np.random.uniform(0, numSamples))
        centers[i, :] = dataSet[index, :]
    print(centers)
    return centers

def Dist2Centers(sample, centers):
    k = centers.shape[0]
    dis2cents = np.zeros(k)
    for i in range(k):
        dis2cents[i] = np.sqrt(np.sum(np.power(sample-centers[i,:], 2)))
    return dis2cents


# showCluster 函数中, 利用matplotlib库的plot函数将不同类别数据以不同颜色显示出来
def showCluster(dataSet, k, centers, clusterAssigmentResult):
    numSamples, dim = dataSet.shape
    mark = ['or', 'ob', 'og', 'om']
    # draw all samples
    for i in range(numSamples):
        markIndex = int(clusterAssigmentResult[i])
        plt.plot(dataSet[i, 0], dataSet[i,1], mark[markIndex])

    mark = ['Dr', 'Db', 'Dg', 'Dm']
    # draw the centroids
    for i in range(k):
        plt.plot(centers[i, 0], centers[i, 1], mark[i], markersize = 17)

    plt.show()
def kmeans(dataSet, k, iterNum):
    numSamples = dataSet.shape[0]
    iterCount = 0
    # clusterAssigmentResult stroes which cluster this sample belongs to
    clusterAssigmentResult = np.zeros(numSamples)
    clusterChanged = True

    # setp1: initialize centers
    centers = initCenters(dataSet, k)
    while clusterChanged and iterCount<iterNum:
        clusterChanged = False
        iterCount = iterCount + 1
        ## for each sample
        for i in range(numSamples):
            dis2cent = Dist2Centers(dataSet[i,:], centers)
            minIndex = np.argmin(dis2cent)
            ## step3: update its belong cluster
            if clusterAssigmentResult[i] != minIndex:
                clusterChanged = True
                clusterAssigmentResult[i] = minIndex

        ## step4: update centers
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssigmentResult[:] == j)[0]]
            centers[j, :] = np.mean(pointsInCluster, axis=0)

    print('Congratulations, Cluster Achieved!')
    return centers, clusterAssigmentResult
def main():
    ##step1:load dataSet
    print('step1: loading data...')
    dataSet = []
    dataSetFile = open('./testSet.txt');
    for line in dataSetFile:
        lineArr = line.strip().split('\t')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
    ##setp2: clusting...
    print('setp2: clusting...')
    dataSet= np.mat(dataSet)

    k = 4
    centersResult, clusterAssigmentResult = kmeans(dataSet, k, 100)

    ##setp3: show the result
    print('setp3: show the result')
    showCluster(dataSet, k, centersResult, clusterAssigmentResult)

main()