#ANOVA ONE WAY CLASSIFICATION
import scipy.stats as stats
print("Enter number of treatments")
t=int(input())
print("enter level of significance")
los=float(input())
rss=0
cf=0
g=0
n=0
ti2=0
for i in range(t):
    l=list(int(x) for x in input().split())
    g+=(sum(l))
    ti2+=((sum(l)*sum(l))/len(l))
    #print(ti2)
    for j in range(len(l)):
        rss+=(l[j]*l[j])
    n+=len(l)    

cf=(g*g)/n
sst=rss-cf
sstr=ti2-cf
sse=sst-sstr
#print(ti2)
print(rss)
print(cf)
print(sst)
print(sstr)
print(sse)

#DEGREES OF FREEDOM
doftr=t-1
dofe=n-t

#MEAN SUM OF SQUARES
msostr=sstr/doftr
msose=sse/dofe

#VARIENCE RATIO
f=msostr/msose

print("The calculated value of F is ",f)

print("The table value of F is ",stats.f.ppf(1-los,doftr,dofe))

if f>stats.f.ppf(1-los,doftr,dofe):
    print("we reject Ho")
else:
    print("we accept Ho")
