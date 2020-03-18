# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:40:49 2020

@author: hzc
"""

from numpy import*
import operator

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

group,labels = createDataSet()

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print(diffMat)
    sqDiffMat = diffMat**2
    print(sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1) #没有axis参数表示全部相加，axis＝0表示按列相加，axis＝1表示按照行的方向相加
    print(sqDistances)
    distances = sqDistances**0.5
    print(distances)
    sortedDistIndicies = distances.argsort() #argsort其实是返回array排序后的下标（或索引）
    print(sortedDistIndicies)    
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        print(voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
        print(classCount)
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    print(sortedClassCount)
    return sortedClassCount[0][0]

print(classify0([0,0],group,labels,3))