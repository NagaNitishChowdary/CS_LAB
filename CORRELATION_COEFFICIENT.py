import numpy as knnc
import math

#x1=list(int(x) for x in input().split())
#x1=[3,7,4,2,0,4,1,2]
x1=[65,66,67,67,68,69,70,72]
x=knnc.array(x1)

#y1=list(int(x) for x in input().split())
#y1=[11,18,9,4,7,6,3,8]
y1=[67,68,65,68,72,72,69,71]
y=knnc.array(y1)

#print(x)
#print(y)

meanOfX=0
sumOfX=0
sumOfXsquare=0
for i in range(len(x)):
    meanOfX+=x[i]
    sumOfXsquare+=(x[i]**2)
sumOfX=meanOfX    
meanOfX/=len(x)
print("meanOfX is ",meanOfX)

meanOfY=0
sumOfY=0
sumOfYsquare=0
for i in range(len(y)):
    meanOfY+=y[i]
    sumOfYsquare+=(y[i]**2)
sumOfY=meanOfY    
meanOfY/=len(y)
print("meanOfY is ",meanOfY)

print("sumOfX is ",sumOfX)

print("sumOfY is ",sumOfY)

sumOfXY=0
for i in range(len(x)):
    sumOfXY+=(x[i]*y[i])
print("sumOfXY is ",sumOfXY)

print("sumOfXsquare is ",sumOfXsquare)

print("sumOfYsquare is ",sumOfYsquare)

covarienceOfXY=(sumOfXY/len(x))-(meanOfX*meanOfY)
print("covarienceOfXY is ",covarienceOfXY)

sigmaX=math.sqrt((sumOfXsquare/len(x))-(meanOfX**2))
sigmaY=math.sqrt((sumOfYsquare/len(y))-(meanOfY**2))
print("sigmaX is ",sigmaX)
print("sigmaY is ",sigmaY)

correlationCoefficient=covarienceOfXY/(sigmaY*sigmaX)
print("correlationCoefficient is ",correlationCoefficient)
