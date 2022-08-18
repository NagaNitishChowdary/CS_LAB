x=list(int(x) for x in input().split())
y=list(int(x) for x in input().split())

x1=x.copy()
x1.sort(reverse=True)

cf1=[]
cf2=[]
cf11=set()
cf22=set()
lx=len(x)
ly=len(y)

rx=[]
q=0
for i in range(lx):
    d=x.count(x[i])
    if d==1:
        rx.append(x1.index(x[i])+1)
    else:
        cf1.append(x[i])
        cf11.add(x[i])
        k=x1.index(x[i])+1
        sum=0
        for j in range(d):
            sum+=(k+j)
        sum/=d
        rx.append(sum)
        #cf1.append(x[i])
        
        
print(rx)        
#print(cf)
y1=y.copy()
y1.sort(reverse=True)

ry=[]
q=0
for i in range(len(y)):
    d=y.count(y[i])
    if d==1:
        ry.append(y1.index(y[i])+1)
    else:
        cf2.append(y[i])
        cf22.add(y[i])
        k=y1.index(y[i])+1
        sum=0
        for j in range(d):
            sum+=(k+j)
        sum/=d
        ry.append(sum)
        #cf2.append(y[i+1])
print(ry)     

di2=[]
sumdi2=0

for i in range(lx):
    di2.append((rx[i]-ry[i])*(rx[i]-ry[i]))
    sumdi2+=((rx[i]-ry[i])*(rx[i]-ry[i]))

cf11=list(cf11)
cf22=list(cf22)

#print(sumdi2)
#print(cf1)
#print(cf11)
#print(cf2)
#print(cf22)

for i in range(len(cf11)):
    k=cf1.count(cf11[i])
    sumdi2+=((k*(k**2-1))/12)

for i in range(len(cf22)):
    k=cf2.count(cf22[i])
    sumdi2+=((k*(k**2-1))/12)

rcc=1-(6*sumdi2)/(lx*(lx**2-1))

print("The rank correlation coefficient is ",rcc)
