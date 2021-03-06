#treePlotter
# -*- coding: utf-8 -*-
#python 2.7

import matplotlib.pyplot as plt
import sys

decisionNode = dict(boxstyle = "sawtooth", fc="0.8")
leafNode = dict(boxstyle = "round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy= parentPt,\
		xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',\
		va= "center", ha="center", bbox= nodeType, arrowprops= arrow_args)

def createPlot():
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	createPlot.ax1= plt.subplot(111,frameon= False)
	plotNode('决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode('叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
	plt.show()


def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			numLeafs += getNumLeafs(secondDict[key])
		else:  numLeafs +=1
	return numLeafs

def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]
	for key in secondDict.keys():
		if type(secondDict[key]).__name__=='dict':
			thisDepth = 1+ getTreeDepth(secondDict[key])
		else: thisDepth = 1
		if thisDepth > maxDepth : maxDepth = thisDepth
	return maxDepth

def retrieveTree(i):
	listofTrees = [{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},\
	{'no surfaing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'},1:'no'}}}}}]

	return listofTrees[i]

def plotMidText(cntrPt, parentPt,txtString):
	xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]
	createPlot.ax1.text(xMid,yMid, txtString)

# def plotTree(myTree, parentPt, nodeTxt):
# 	numLeafs = getNumLeafs(myTree)
# 	depth = getTreeDepth(myTree)
# 	firstStr = myTree.keys()[0]
# 	cntrPt = (plotTree.xoff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,\
# 		plotTree.yoff)
#     plotMidText(cntrPt, parentPt, nodeTxt)
#     plotNode(firstStr, cntrPt, parentPt, decisionNode)
#     secondDict = myTree[firstStr]
#     plotTree.yoff = plotTree.yoff - 1.0/plotTree.totalD
#     for key in secondDict.keys():
#     	if type(secondDict[key]).__name__=='dict':
#     		plotTree(secondDict[key]), cntrPt, str(key)
#     	else:
#     		plotTree.xoff = 

#myTree=retrieveTree(0)

#get number of leaf and depth
#getNumLeafs(myTree)
#getTreeDepth(myTree)



   

    
