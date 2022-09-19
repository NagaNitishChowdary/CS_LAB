# LINEAR DISCRIMINANT ANALYSIS

import numpy as np
import math 

def zero_matrix(rows,cols):
  Az=[]
  for i in range(rows):
    Az.append([])
    for j in range(cols):
      Az[-1].append(0.0)
  return Az

def transpose(Az):
  Bz=zero_matrix(len(Az[0]),len(Az))
  for i in range(len(Az)):
    for j in range(len(Az[0])):
      Bz[j][i]=Az[i][j]
  return Bz

def multiply(Az,Bz):
  Cz=zero_matrix(len(Az),len(Bz[0]))
  for i in range(len(Az)):
    for j in range(len(Bz[0])):
      for k in range(len(Bz)):
        Cz[i][j]+=(Az[i][k]*Bz[k][j])
  return Cz

def cofactor(m,i,j):
  return ([row[:j]+row[:j+1]] for row in (mat[:i]+mat[i+1:]))

def det(A):
  if(len(A)==2):
    return A[0][0]*A[1][1]-A[1][0]*A[0][1]
  sum1=0
  for knnc in range(len(A)):
    sign=(-1)**knnc
    sub_set=det(cofactor(A,0,knnc))
    sum1+=sign*A[0][knnc]*sub_set
  return sum1                    


#l1=list(float(x) for x in input().split())
#l2=list(float(x) for x in input().split())
#l1=[2.95,2.53,3.57,3.16,2.58,2.16,3.27]
#l2=[6.63,7.79,5.65,5.47,4.46,6.22,3.52]
l1=[4.0,2.0,2.0,3.0,4.0,9.0,6.0,9.0,8.0,10.0]
l2=[2.0,4.0,3.0,6.0,4.0,10.0,8.0,5.0,7.0,8.0]


#xk=[]
#xk=list(float(x) for x in input().split())
xk=[[5.0],[6.0]]

x=[]
for i in range(len(l1)):
  x.append([l1[i],l2[i]])

print(x)  

#y=[]
#y=list(int(x) for x in input().split())
y=[1,1,1,1,1,0,0,0,0,0]

x1=[]
x2=[]
mean01=mean02=0
for i in range(len(y)):
  if(y[0]==y[i]):
    x1.append(x[i])
  else:
    x2.append(x[i])
  mean01+=x[i][0]
  mean02+=x[i][1]
mean01/=len(y)
mean02/=len(y)


#mean=[]
#mean1=[]
#mean2=[]
mean11=mean12=mean21=mean22=0

for i in range(len(x1)):
  mean11+=x1[i][0]
  mean12+=x1[i][1]
mean11/=len(x1)
mean12/=len(x1)

for i in range(len(x2)):
  mean21+=x2[i][0]
  mean22+=x2[i][1]
mean21/=len(x2)
mean22/=len(x2)

meanx=[mean01,mean02]
meanx1=[mean11,mean12]
meanx2=[mean21,mean22]

xminusu=[]
for i in range(len(x)):
  xminusu.append([x[i][0]-meanx[0],x[i][1]-meanx[1]])
print(xminusu)  

print(meanx1)
print(meanx2)
print(meanx)

meanx1=[[mean11,mean12]]
meanx2=[[mean21,mean22]]
meanx1=np.array(meanx1)
meanx2=np.array(meanx2)
xk=np.array(xk)
#print(x)
xminusutrans=transpose(xminusu)
c=multiply(xminusutrans,xminusu)

for i in range(len(c)):
  for j in range(len(c[0])):
    c[i][j]/=len(y)

print("c= ",c)    

cinverse=np.linalg.inv(c)
print("cinverse = ",cinverse)

# FISHER'S LINEAR DISCRIMINANT FUNCTION
#print(meanx1)
#d=np.matmul(meanx1,cinverse)
#print(d)
#print(xk)
d=np.matmul(meanx1,cinverse)
#print(d)
#e=multiply(d,xk)
#e=list(e)
#print(e[0][0])
f1=multiply(multiply(meanx1,cinverse),xk)[0][0]-((multiply(multiply(meanx1,cinverse),meanx1.T))[0][0])*0.5+math.log(len(x1)/len(x))
f2=multiply(multiply(meanx2,cinverse),xk)[0][0]-((multiply(multiply(meanx2,cinverse),meanx2.T))[0][0])*0.5+math.log(len(x2)/len(x))

print("f1=",f1)
print("f2=",f2)

if f2>f1:
  print("WE CLASSIFY THEM INTO SECOND GROUP")
else:
  print("WE CLASSIFY THEM INTO FIRST GROUP")

#print(math.log(5/10))
