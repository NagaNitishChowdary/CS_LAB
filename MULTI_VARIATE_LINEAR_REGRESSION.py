import numpy as np


def copy_matrix(M):
  rows = len(M)
  cols = len(M[0])
  MC = zeros_matrix(rows, cols)
  for i in range(rows):
      for j in range(rows):
          MC[i][j] = M[i][j]
  return MC

def getcofactor(m, i, j):
  return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]

def determinantOfMatrix(mat):
  if(len(mat) == 2):
    value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
    return value
  Sum = 0
  for current_column in range(len(mat)):
      sign = (-1) ** (current_column)
      sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
      Sum += (sign * mat[0][current_column] * sub_det)
  return Sum

def zeros_matrix(rows, cols):
  A = []
  for i in range(rows):
      A.append([])
      for j in range(cols):
          A[-1].append(0.0)
  return A

def transpose(A):
  m=len(A)
  n=len(A[0])
  B=zeros_matrix(n, m)
  #B=[[0 for i in range(m)] for j in range(n)]
  for i in range(m):
    for j in range(n):
      B[j][i]=A[i][j]
  return B

def Multiply(A,B):
  result=zeros_matrix(len(A), len(B[0]))
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]
  return result

"""
def identity(B):
  A=[]
  for i in range(len(B)):
      A.append([])
      for j in range(len(B[0])):
          if i==j:
              A[-1].append(1.0)
          else:
              A[-1].append(0.0)
  return A

def inverse(A):
  I=identity(A)
  #print(I)
  AM = copy_matrix(A)
  n = len(A)
  IM = copy_matrix(I)
  indices = list(range(n))
  for fd in range(n):
      fdScaler = 1.0 / AM[fd][fd]
      for j in range(n):
          AM[fd][j] *= fdScaler
          IM[fd][j] *= fdScaler
      for i in indices[0:fd] + indices[fd+1:]:
          crScaler = AM[i][fd]
          for j in range(n):
              AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
              IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
  #print_matrix("the inverse of matix",A)
  #print_matrix("is",IM)
  return IM
"""

#y=int(input("ENTER NO OF DEPENDENT VARIABLES"))
y=2

#y1=[]
#for i in range(y):
  #l=list(int(x) for x in input().split())
  #y1.append(l)
y1=[[10.0,12.0,11.0,9.0,9.0,10.0,11.0,12.0,11.0,10.0,11.0,12.0],[100.0,110.0,105.0,94.0,95.0,99.0,104.0,108.0,105.0,98.0,103.0,110.0]]
y11=np.array(y1)
#y1=y11.T
y1=transpose(y11)
#print(y1)

#x=int(input("ENTER NO OF INDEPEN"))  
x=3

#x1=[[1 for i in range(len(y1[0]))]]
#for i in range(x):
  #l=list(int(x) for x in input().split())
  #x1.append(l)
x1=[[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],[9.0,8.0,7.0,14.0,12.0,10.0,7.0,4.0,6.0,5.0,7.0,6.0],[62.0,58.0,64.0,60.0,63.0,57.0,55.0,56.0,59.0,61.0,57.0,60.0],[1.0,1.3,1.2,0.8,0.8,0.9,1.0,1.2,1.1,1.0,1.2,1.2]]
x11=np.array(x1)
#x1=x11.T
x1=transpose(x11)
#print(x1)

#x11=np.array(x1)
#x1=x11.T
#x1=np.array(x1)
#y11=np.array(y1)
#y1=y11.T
#y1=np.array(y1)
#xt=x1.T
xt=transpose(x1)
#xtx=np.matmul(xt,x1)
xtx=Multiply(xt,x1)
#print(xtx)
xtxinv=np.linalg.inv(xtx)
#xtxinv=inverse(xtx)
#xty=np.matmul(xt,y1) 
xty=Multiply(xt,y1)
#beta=np.matmul(xtxinv,xty)
beta=Multiply(xtxinv,xty)
for i in range(len(beta)):
  print(beta[i])

