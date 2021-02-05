# 2.2차원 리스트로 이루어진 행렬 A와 B에 대해 함수 multiplyMatrix(A, B)를 사용하여
# 두 행렬에 대한 곱셈 연산을 실행하는 프로그램을 작성하라.
def multiplymatrix(A,B,C):
   for i in range(0,len(C)):
       for j in range(0,L):
           s=0
           for k in range(0,M):
               s+=A[i][k]*B[k][j]
           C[i][j]=s
   printMatrix(C)



L=int(input('L:'))
M=int(input('M:'))
N=int(input('N:'))
A=[]
B=[]
C=[]
for i in range(L):
    c=[]
    for j in range(N):
        c.append(0)
    C.append(c)

import random
for i in range(L):
    a=[]
    for j in range(M):
        a.append(random.randint(-3,3))
    A.append(a)
def printMatrix(A):
    for i in range(L):
        for j in range(M):
            print(A[i][j],end=' ')
        print("")
print('행렬 A')
printMatrix(A)
print('')
for i in range(M):
    b=[]
    for j in range(N):
        b.append(random.randint(-3,3))
    B.append(b)
def printMatrix(B):
    for i in range(M):
        for j in range(N):
            print(B[i][j],end=' ')
        print("")
def printMatrix(C):
    for i in range(len(C)):
        for j in range(len(C)):
            print(C[i][j],end=' ')
        print("")
print('행렬 B')
printMatrix(B)
print('')
print('행렬 A*B')
multiplymatrix(A,B,C)
