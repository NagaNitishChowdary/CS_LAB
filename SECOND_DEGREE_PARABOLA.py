import numpy as np
import matplotlib.pyplot as plt

# x=list(float(x) for x in input().split())
# y=list(float(x) for x in input().split())
x=[2,4,6,8,10]
y=[3.07,12.85,31.47,57.38,91.29]

x=np.array(x)
y=np.array(y)
x2=x**2
x3=x**3
x4=x**4
xy=x*y
x2y=x2*y

c=[sum(y),sum(xy),sum(x2y)]
c1=[len(x),sum(x),sum(x2)]
c2=[sum(x),sum(x2),sum(x3)]
c3=[sum(x2),sum(x3),sum(x4)]

d=np.column_stack((c1,c2,c3))
d1=np.column_stack((c,c2,c3))
d2=np.column_stack((c1,c,c3))
d3=np.column_stack((c1,c2,c))

a=np.linalg.det(d1)/np.linalg.det(d)
b=np.linalg.det(d2)/np.linalg.det(d)
c=np.linalg.det(d3)/np.linalg.det(d)

print("the second degree parabola is : y=",round(a,4),"+",round(b,4),"x+",round(c,4),"*x*x")
plt.plot(x,a+b*x+c*x*x,color="red")
plt.scatter(x,y,color="blue")
plt.xlabel('x',color="red")
plt.ylabel('y',color="red")
plt.grid()
plt.show()
