#kmeans algorithm
# -*- coding: utf-8 -*-

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt 

def createDataSet():
	group = array ([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group, labels


	#group, labels = kNN.createDataSet() # how to define the group and print it?

	#print(group,labels)


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet  # tile([a],(3,2)) means 矩阵元素重复3 raw,2 column.   两次[a,a],并重复三行 [[a,a],[a,a],[a,a]]
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort() #return the index of distance from short to long
	classCount = {}
	print(type(classCount))
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	print(classCount.items())
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1),reverse=True) #operator.itemgetter(1)获取对象的第1个域的值
	return sortedClassCount[0][0] # 0raw 0 column

    # print(classify0([0,0],group,labels,3))

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOLines = len(arrayOLines)
	returnMat = zeros((numberOLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return  returnMat, classLabelVector


def autoNorm(dataset):
    minVals = dataset.min(0)
    maxVals = dataset.max(0)
    ranges = maxVals - minVals 
    normDataSet = zeros(shape(dataset))
    m = dataset.shape[0]
    normDataSet = dataset - tile(minVals,(m,1))
    normDataSet = normDataSet/tile(ranges,(m,1))
    return  normDataSet, ranges, minVals

def datingClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels=file2matrix('datingTestSet2.txt')
	normMat,ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
	    classiferResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],\
	    	datingLabels[numTestVecs:m],3)
	    print "the classifier came back with: %d, the real answer is: %d" \
	        % (classiferResult,datingLabels[i])
	    if (classiferResult != datingLabels[i]): errorCount +=1
	print "the total error rate is: %f" % (errorCount/float(numTestVecs))

def classifyperson():
    resultList = ['not at all', 'in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games?"))
    ffMiles = float(raw_input("frequency filter miles earned per year?"))
    iceCream = float(raw_input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
    normMat,ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles,percentTats,iceCream])
    classiferResult = classify0((inArr - minVals)/ranges,normMat, datingLabels,3)
    print "you will probably like this person: ",resultList[classiferResult - 1]
    


	






#run code
if __name__=="__main__":
 group,labels = createDataSet()
 print (classify0([0,0],group,labels,3))
 # datingDataMat,datingLabels=kNN.file2matrix('datingTestSet2.txt')
 # print (datingDataMat,datingLabels[0:20])
 #
 # fig = plt.figure()
 # ax = fig.add_subplot(111)
 # ax.scatter(datingDataMat[:1],datingDataMat[:2])
 #ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
 # plt.show







