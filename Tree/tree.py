# tree algorithm
# -*- coding: utf-8 -*-
from math import log
import operator
from treePlotter import *

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet: #?
		currentLabel = featVec[-1]
		if currentLabel  not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] +=1 #?
	shannonEnt = 0.0
	for key in labelCounts :
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log (prob,2)
	return  shannonEnt

def createDataSet():
	dataSet =[[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet, labels 

def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0])-1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0;bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i 
	return bestFeature

def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.key(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),\
		key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]

def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0])==1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value  in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet\
			(dataSet,bestFeat,value),subLabels)
	return myTree

def classify(inputTree, featLabels, testVec):
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featLabels] == key:
			if type(secondDict[key]).__name__=='dict':
				classLabel = classify(secondDict[key], featLabels, testVec)
			else:
				classLadel = secondDict[key]
	return classLadel

def storeTree(inputTree, filename):
	import pickle
	fw = open(filename,'w')
	pickle.dump(inputTree,fw)
	fw.close 

def grabTree(filename):
	import pickle
	fr = open(filename)
	return pickle.load(fr)









if __name__ == "__main__":
    myDat,labels = createDataSet()
    calcShannonEnt(myDat)
	#myDat, labels = tree.createDataSet()
	#tree.chooseBestFeatureToSplit(myDat)
    print(myDat)
    myTree = retrieveTree(0)
    print(myTree)
    storeTree(myTree, 'classifierStorage.txt')
    
    classify(myTree,labels,[1,0])
    classify(myTree,labels,[1,1])

    storeTree(myTree, 'classifierStorage.txt')
    grabTree('classifierStorage.txt')

    # main()

	#python中的小括号( )：代表tuple元组数据类型，元组是一种不可变序列 tup = (1,2,3)
	#python中的中括号[]：代表list列表数据类型，列表是一种可变的序列。list('python') ['p', 'y', 't', 'h', 'o', 'n']
   # python大括号{ }花括号：代表dict字典数据类型，字典是由键对值组组成。冒号':'分开键和值，逗号','隔开组。dic={'jon':'boy','lili':'girl'}