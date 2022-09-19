# MANOVA

import numpy as np
import pandas as pd
import scipy.stats as stats
import math

#t=[]
t=3
#for _ in range(int(input('Enter no of treatments:'))):
  #l=int(input("enter no of lists"))
  #tr=[]
  #for i in range(l):
    #tr.append(list(int(x) for x in input().split()))
  #t.append(tr)

y=[[[9,3],[6,2],[9,7]],[[0,4],[2,0]],[[3,8],[1,9],[2,7]]]
print(y) 

t1=[]
for i in y:
  t1.extend(i)

#print(t1)

y1=[]
for i in y:
  a=np.array(i)
  b=np.mean(a,axis=0)
  y1.append(list(b))
print(y1) 

y11=[]
a=np.array(t1)
b=np.mean(a,axis=0)
y11.append(list(b))
print(y11)

# FOR Y1

# SUM OF SQUARES DUE TO ERROR(SSE1)
sse1=0
for i in range(t):
  for j in range(len(y[i])):
    sse1+=(y[i][j][0]-y1[i][0])**2
  #print(sse1)  
#print(type(sse1))    
print("sse1=",sse1)
#print(type(y))
#print(type(y1))

# SUM OF SQUARES DUE TO TOTAL(SST)
#print(y11)
sst1=0
for i in range(t):
  for j in range(len(y[i])):
    sst1+=(y[i][j][0]-y11[0][0])**2
print("sst1=",sst1)    

# SUM OF SQUARES DUE TO REGRESSION
ssr1=sst1-sse1
print("ssr1=",ssr1)

# FOR Y2

# SUM OF SQUARES DUE TO ERROR(SSE2)
sse2=0
for i in range(t):
  for j in range(len(y[i])):
    sse2+=(y[i][j][1]-y1[i][1])**2
  #print(sse2)  
#print(type(sse2))    
print("sse2=",sse2)

# SUM OF SQUARES DUE TO TOTAL(SST2)
#print(y11)
sst2=0
for i in range(t):
  for j in range(len(y[i])):
    sst2+=(y[i][j][1]-y11[0][1])**2
print("sst2=",sst2)    

# SUM OF SQUARES DUE TO REGRESSION(SSR2)
ssr2=sst2-sse2
print("ssr2=",ssr2)


# CROSS PRODUCT OF Y1 AND Y2


# SUM OF SQUARES DUE TO ERROR(SSE12)
sse12=0
for i in range(t):
  for j in range(len(y[i])):
    sse12+=(y[i][j][0]*y[i][j][1])-(y1[i][0]*y1[i][1])
print("sse12=",sse12)

# SUM OF SQUARES DUE TO TOTAL(SST12)
sst12=0
for i in range(t):
  for j in range(len(y[i])):
    sst12+=(y[i][j][0]*y[i][j][1])-(y11[0][0]*y11[0][1])
print("sst12=",sst12)

# SUM OF SQUARES DUE TO REGRESSION
ssr12=sst12-sse12
print("ssr12=",ssr12)


B=[[ssr1,ssr12],[ssr12,ssr2]]
W=[[sse1,sse12],[sse12,sse2]]
T=[[sst1,sst12],[sst12,sst2]]

def cofactor(m,i,j):
  return ([row[:j]+row[j+1:]] for row in (m[:i]+m[i+1:]))

def det(A):
  if(len(A)==2):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
  sum1=0
  for knnc in range(len(A)):
    sign=(-1)**knnc
    sub_set=det(cofactor(A,0,knnc))
    sum1+=sign*A[0][knnc]*sub_set
  return sum1      

n=len(t1)
#print(n)

# MANOVA ONE WAY CLASSIFICATION TABLE 
df=pd.DataFrame()
df["SOURCE OF VARIATION"]=["REGRESSION","ERROR","TOTAL"]
df["SUM OF SQUARES"]=[B,W,T]
df["DEGREES OF FREEDOM"]=[t-1,n-t,n-1]
df["WILLS VALUES"]=["*",det(W)/det(T),"*"]
df["F-TEST"]=["*",((n-t-1)/(t-1))*((1-math.sqrt(det(W)/det(T)))/math.sqrt(det(W)/det(T))),"*"]
fcal=((n-t-1)/(t-1))*((1-math.sqrt(det(W)/det(T)))/math.sqrt(det(W)/det(T)))

print(df)

alpha=0.05
ftab=stats.f.ppf(1-alpha,(t-1)*(t-1),(t-1)*(n-t-1))

if fcal>ftab:
  print("WE REJECT H0")
  print("HENCE WE CONCLUDE THAT THERE IS NO HOMOGENITY AMONG THE TREATMENTS")
else:
  print("WE ACCEPT H0")
  print("HENCE WE CONCLUDE THAT THER IS HOMOGENITY AMONG THE GROUPS")  
