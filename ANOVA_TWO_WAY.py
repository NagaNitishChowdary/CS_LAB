#ANOVA TWO WAY CLASSIFICATION
import scipy.stats as stats

print("Enter number of treatments")
#k=int(input())
k=3

print("Enter level of Significance")
#los=float(input())
los=0.05

rss=0
g=0
sst=0;
sstr=0;
ssb=0;
sse=0;
ti2=0;
bj2=0;
l1=[]
for i in range(k):
    l=list(int(x) for x in input().split())
    for j in range(len(l)):
        rss+=(l[j]*l[j])
    g+=sum(l)
    ti2+=(sum(l)*sum(l))
    l1.append(l)

h=len(l1[0])
for i in range(h):
    bj=0
    for j in range(k):
        #bj2+=(l1[j][i]*l1[j][i]
        bj+=l1[j][i]
    bj2+=(bj*bj)    
        
        
#h=len(l1[0])
cf=(g*g)/(k*h)
sst=rss-cf
sstr=(ti2)/h-cf
ssb=(bj2)/k-cf
sse=sst-sstr-ssb
#print(bj2)
print(rss)
print(cf)
print(sst)
print(sstr)
print(ssb)
print(sse)

doftr=k-1
dofb=h-1
dofe=doftr*dofb

msostr=sstr/doftr 
msosb=ssb/dofb 
msose=sse/dofe 

ftr=msostr/msose 
fb=msosb/msose 

print("The calculated value of f due to treatments is ",ftr)

print("The table value of f due to treatments is ",stats.f.ppf(1-los,doftr,dofe))

print("The calculated value of f due to blocks is ",fb)

print("The table value of f due to blocks is ",stats.f.ppf(1-los,dofb,dofe))    
      
if(ftr<stats.f.ppf(1-los,doftr,dofe)):
    print("WE ACCEPT H0(tr)")
    print("THERE IS HOMOGENITY AMONG THE TREATMENTS")
else:
    print("WE REJECT H0(tr)")
    print("THERE IS NO HOMOGENITY AMONG THE TREATMENTS") 
    
if(fb<stats.f.ppf(1-los,dofb,dofe)):
    print("WE ACCEPT H0(b)")
    print("THERE IS HOMOGENITY AMONG THE BLOCKS")
else:
    print("WE REJECT H0(b)")
    print("THERE IS NO HOMOGENITY AMONG THE BLOCKS")   
