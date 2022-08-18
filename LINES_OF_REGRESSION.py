#LINES OF REGRESSION

import numpy as np 
import math

#x1=list(int(x) for x in input().split())
x1=[2,5,3,4,9,12]
x=np.array(x1)

#y1=list(int(x) for x in input().split())
y1=[12,8,6,8,4,5]
y=np.array(y1)

#print(x)
#print(y)

sumOfX=0
meanOfX=0
sumOfXsquare=0
for i in range(len(x)):
    sumOfX+=x[i]
    sumOfXsquare+=(x[i]**2)
meanOfX=sumOfX/len(x)

sumOfY=0
sumOfYsquare=0
meanOfY=0
for i in range(len(y)):
    sumOfY+=y[i]
    sumOfYsquare+=(y[i]**2)
meanOfY=sumOfY/len(y)

sumOfXY=0
for i in range(len(x)):
    sumOfXY+=(x[i]*y[i])

print("meanOfX is ",meanOfX)
print("meanOfY is ",meanOfY)

print("sumOfX is ",sumOfX)
print("sumOfY is ",sumOfY)

print("sumOfXsquare is ",sumOfXsquare)
print("sumOfYsquare is ",sumOfYsquare)

print("sumOfXY is ",sumOfXY)

covarienceOfXY=(sumOfXY/len(x))-(meanOfX*meanOfY)
print("covarienceOfXY is ",covarienceOfXY)

sigmaX=math.sqrt((sumOfXsquare/len(x))-(meanOfX**2))
sigmaY=math.sqrt((sumOfYsquare/len(y))-(meanOfY**2))
print("sigmaX is ",sigmaX)
print("sigmaY is ",sigmaY)

correlationCoefficient=covarienceOfXY/(sigmaY*sigmaX)
print("correlationCoefficient is ",correlationCoefficient)

regressionCoefficientXonY=(correlationCoefficient*sigmaX)/sigmaY
print(regressionCoefficientXonY)

regressionCoefficientYonX=(correlationCoefficient*sigmaY)/sigmaX
print(regressionCoefficientYonX)

#REGRESSION LINE X ON Y  
print("x = ",regressionCoefficientXonY,"y + ",(-regressionCoefficientXonY*meanOfY)+meanOfX)

#REGRESSION LINE Y ON X
print("y = ",regressionCoefficientYonX,"x + ",(-regressionCoefficientYonX*meanOfX)+meanOfY)
