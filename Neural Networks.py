import json
import sys
import numpy
from myMethods import *


def printm(matrix):
    try:
        if type(matrix[0]) == list:
            for row in matrix:
                print(numpy.array(row))
        elif type(matrix) == list:
            print(numpy.array(matrix))
    except Exception:
        if type(matrix) == list:
            print(numpy.array(matrix))
        else:
            print(matrix)
    print("")

def printv(a="", b="", c="", d="", e="", f="", g="", h="", i="", j=""):
    print("info: ")
    print(a, b, end=" ")
    print(c, d, end=" ")
    print(e, f, end=" ")
    print(g, h, end=" ")
    print(i, j, end=" ")
    print("")


def makeList(data,input):
    collection=[]
    layer = 0
    for i in data:
        collection.append([])
        size_in = int(data[i]["size_in"])
        size_out = int(data[i]["size_out"])
        weights = data[i]["weights"]

        for x in range(size_out):
            collection[layer].append([])
            for y in range(size_in):
                collection[layer][x].append(0)

        for node in weights:
            nextNodes=weights[node]
            for nextNode in nextNodes:
                collection[layer][int(nextNode)-1][int(node)-1]=nextNodes[nextNode]
        layer+=1
    return collection

def makeEmptyMatrix(rows,columns):
    matrix=[]
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(0)
    return matrix


def dotProduct(matrixes,resultaat=[]):
    if len(matrixes)==0:
        return resultaat

    index1=len(matrixes)-1    #index of second matrix
    index2=len(matrixes)-2    #index of first matrix
    newMatrix = makeEmptyMatrix(len(matrixes[index1]), len(matrixes[index2][0]))  # 2x5
    for x in range(len(matrixes[index1])):  # x=rijen van L1 en newMatrix
        for j in range(len(matrixes[index2][0])):       #j=kolommen van L2
            newElement=0
            for i in range(len(matrixes[index1][0])):  # i=kolommen van L1 en newMatrix
                element1=float(matrixes[index1][x][i])
                element2=float(matrixes[index2][i][j])
                newElement+=round(element1*element2,2)
            newMatrix[x][j]=newElement
    matrixes.pop()
    matrixes.pop()
    return dotProduct(matrixes,newMatrix)


def vectorMultiplication(matrix,vector):
    newVector = makeEmptyMatrix(1,len(matrix))[0]
    for i in range(len(matrix)):
        newElement=0
        for j in range(len(vector)):
            element1=float(vector[j])
            element2=float(matrix[i][j])
            newElement+=round(element1*element2,2)
        newVector[i]=newElement
    return newVector


def getInput():
    invoer=input("input vector: ")
    invoer=invoer.replace("]", "").replace("[", "").split(",")
    invoer=typeList(invoer,int)
    return invoer




data=openjs("data.json")

collection=makeList(data,input)
printm(collection)
print("\n")
newMatrix=dotProduct(collection)
printm(newMatrix)
newVector=vectorMultiplication(newMatrix,getInput())
printm(newVector)


