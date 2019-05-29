import numpy as np
from myMethods import *
import math

def scanner():
   while True:
      size = input("give a size (integer) for your Magical Square: ")
      try:
         size=int(size)
         break
      except Exception:
         print("I said an integer!")

   list1=[]
   for j in range(size):
      list1.append([])
      for i in range(size):
         while True:
            number=input("x"+str(j+1)+str(i+1)+":")
            if number=="":
               number=0
            else:
               try:
                  number=int(number)
               except Exception:
                  print("try again")
                  continue
            list1[j].append(number)
            break
   printm(list1)
   return list1


def calculateSolutionMatrix(MagicalSquare=[]):
   action = input("use example Magical Square? no/yes ")
   if action.lower() == "no" or action.lower() == "nee":
      MagicalSquare=scanner()
   list1 = []
   resultVec=resultVector(MagicalSquare)
   size = len(MagicalSquare)
   extraRij=0
   if size==3:
      extraRij=1
   aantalRijen=(2 * size) + 2+extraRij
   aantalKolommen=(size ** 2) + 1
   for i in range(aantalRijen):  # aantal rijen zijn 2 keer lengte, plus 2 keer diagonaal plus 3x middelste
      list1.append([])
      for j in range(aantalKolommen):
         list1[i].append(0)

   solution = list1
   magische_row = flatten(MagicalSquare)
   # indeces = row met lengte n
   indeces = []
   n = len(MagicalSquare)
   for i in range(n):
      indeces.append([])

   for row in range(0, aantalRijen):
      for i in range(n):
         if row <= n - 1:
            indeces[i] = n * row + i  # row insertion for first 3 rows: indeces 1,2,3  4,5,6  7,8,9
         elif row <= 2 * n - 1:
            indeces[i] = n * i + (row - n)  # column insertion for 3rd to 6th rows
         elif row == 2 * n:
            indeces[i] = (n + 1) * i  # diagonal from left above to right under
         elif row == 2 * n + 1:
            indeces[i] = (n - 1) * (i + 1)  # diagonal from right above to left under
         elif n % 2 > 0:
            indeces[i] = (2 * n + 2) // 2

      for i in range(n):

         if magische_row[indeces[i]] == 0:
            if row == 2 * n + 2:
               solution[row][indeces[i]] = 3
            else:
               solution[row][indeces[i]] = 1
         else:
            solution[row][indeces[i]] = 0
            resultVec[row]-=magische_row[indeces[i]]
         solution[row][aantalKolommen-1] = -1
   return solution,resultVec



def resultVector(magicSquare):
   vector=[]
   extraRij=0
   if len(magicSquare)==3:
      extraRij+=1
   for i in range((2 * len(magicSquare)) + 2 + extraRij):
      vector.append(0)
   return vector



def flatten(magicSquare):
   list=[]
   for i in magicSquare:
      for j in i:
         list.append(j)
   return list

def fillMagicalSquare(matrix,resultvector):
   ms=np.dot(np.linalg.pinv(matrix), resultvector)
   return ms




A=[[0,1,1,0,0,0,0,0,0,-1],
   [0,0,0,1,1,0,0,0,0,-1],
   [0,0,0,0,0,0,1,1,0,-1],
   [0,0,0,1,0,0,1,0,0,-1],
   [0,1,0,0,1,0,0,1,0,-1],
   [0,0,1,0,0,0,0,0,0,-1],
   [0,0,0,0,1,0,0,0,0,-1],
   [0,0,1,0,1,0,1,0,0,-1],
   [0,0,0,0,3,0,0,0,0,-1]]

C=[-5,-4,-6,-5,0,-10,-11,0,0]

ms_example=[[5,0,0],[0,0,4],[0,0,6]]
ms_ex2=[[1,1,1],[1,1,1],[1,1,1]]



solution,resultVec=calculateSolutionMatrix(ms_example)
printm(solution)
printm(resultVec)

ms=fillMagicalSquare(solution,resultVec)
print(ms)
