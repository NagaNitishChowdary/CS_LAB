# PRINCIPAL COMPONENT ANALYSIS

import math 
import numpy as np
import pandas as pd

#p=int(input("ENTER NO OF VARIABLES"))
p=3

#x=[]
#for i in range(p):
  #l=list(float(x) for x in input().split())
  #x.append(l)
#print(x)  
x=[[7,4,6,8,8,7,5,9,7,8],[4,1,3,6,5,2,3,5,4,2],[3,8,5,1,7,9,3,8,5,2]]

def zero_matrix(rows,cols):
  A=[]
  for i in range(rows):
    A.append([])
    for j in range(cols):
      A[-1].append(0.0)
  return A    

def transpose(A):
  B=zero_matrix(len(A[0]),len(A))
  for i in range(len(A)):
    for j in range(len(A[0])):
      B[j][i]=A[i][j]
  return B

def multiply(A,B):
  C=zero_matrix(len(A),len(B[0]))
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        C[i][j]+=A[i][k]*B[k][j]
  return C


meanx=[sum(x[0])/len(x[0]),sum(x[1])/len(x[1]),sum(x[2])/len(x[2])]
print(meanx)

#print(transpose(x))  

xminusu=zero_matrix(len(x),len(x[0]))
for i in range(len(x)):
  for j in range(len(x[0])):
    xminusu[i][j]=x[i][j]-meanx[i]
print(xminusu)    

c=multiply(xminusu,transpose(xminusu))
print(c)
for i in range(len(c)):
  for j in range(len(c[0])):
    c[i][j]/=len(x[0])
print(c)    

d=np.linalg.eig(c)
d=list(d)
print(d[1])
