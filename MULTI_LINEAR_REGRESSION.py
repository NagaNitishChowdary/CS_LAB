# MULTILINEAR REGRESSION 

import numpy as np 
import pandas as pd
import scipy.stats as stats 


#print("enter dependent variabels")
#y=list(int(x) for x in input().split())
y=[100,110,105,94,95,99,104,108,105,98,105,110]

#n=int(input("enter no of independent variables"))
p=2
#x=[[1 for x in range(len(y))]]
#for i in range(n):
  #l=list(int(x) for x in input().split())
  #x.append(l)
x=[[1,1,1,1,1,1,1,1,1,1,1,1],[9,8,7,14,12,10,7,4,6,5,7,6],[62,58,64,60,63,57,55,56,59,61,57,60]]

#print(x)
x1=np.array(x)
y1=np.array(y)
c1=x1.T
c2=np.matmul(x1,c1)
c3=np.linalg.inv(c2) 
d=np.matmul(y1,c1)
beta=np.matmul(d,c3)

print(beta)

# TO TEST THE GOODNESS OF FIT OF THE MODEL

ycap=[]
for i in range(len(y)):
  ycap.append(beta[0]+(beta[1]*x[1][i])+(beta[2]*x[2][i]))

print(ycap)

error=[]
for i in range(len(y)):
  error.append(y[i]-ycap[i])

print(error)

sse=0
for i in range(len(error)):
  sse+=(error[i]*error[i])

sst=0
meany=sum(y)/len(y)
for i in range(len(error)):
  sst+=((y[i]-meany)*(y[i]-meany))

#print(sse,sst)

ssr=sst-sse

# r is the coefficient of determination
r=ssr/sst
print(r)

print("inference")
if(r>0.9):
  print("we say that model is a good fit")
else:
  print("we say that model is not a good fit")

# GOODNESS OF FIT TO TEST THE REGRESSION MODEL USING ANOVA TEST

#alpha=float(input("enter level of significance(enter 0 if not given"))
alpha=0
if(alpha==0):
  alpha=0.05

df=pd.DataFrame()
df["source of variation"]=["treatments","error","total"]
df["sum of squares"]=[ssr,sse,sst]
df["degrees of freedom"]=[p,len(y)-(p+1),len(y)-1]
msosr=ssr/p
msose=sse/(len(y)-(p+1))
df["mean sum of squares"]=[msosr,msose,"*"]
f=msosr/msose
if(f<1):
  f=1/f
  ftab=stats.f.ppf(1-alpha,len(y)-(p+1),p)
else:
  ftab=stats.f.ppf(1-alpha,p,len(y)-(p+1)) 
df["varience ratio"]=["*",f,"*"]

print(df)

print("the table value is ",ftab)

print("inference")
if(f>=ftab):
    print("Hence we conclude that there are demo variables which are contributing to the model and the given model is a good fit")
    print("To know which variables are more contributing to the model we do test of individual parameters")
else:
    print("Hence we conclude that there are no demo variables which are contributing to the model and the given model is not a good fit")

print('To test the above hypothesis using the test statistic is given by')

# t=beta/(sqrt(msose.cjj))
cjj=[]
for i in range(len(x)):
  cjj.append(c3[i][i])

print(cjj)

msose1=[]
for i in range(len(x)):
  msose1.append((cjj[i]*msose)**0.5)

t=[]
for i in range(len(x)):
  t.append(beta[i]/msose1[i])

df2=pd.DataFrame()

df2["predictor"]=['B'+str(i) for i in range(p+1)]
df2["coefficient"]=[beta[i] for i in range(p+1)]
df2["Standard Error"]=[msose1[i] for i in range(p+1)]
df2["t~t(n-p)"]=[t[i] for i in range(p+1)]

print(df2)

ttab=stats.t.ppf(1-alpha/2,len(y)-(p+1))
print("table value of t at",alpha,"level of signifance and ",alpha,"is ",ttab)

print("Inference")

for i in range(p+1):
  if(abs(t[i])>ttab):
    print("we reject H0")
    print("B"+str(i)+" is contributing to the model")
  else:
    print("we accept H0")
    print("B"+str(i)+" is not contributing to the model")

