from math import *
n = int(input())
A,B,C,D = [0]*n,[0]*n,[0]*n,[0]*n

for i in range(n):
    A[i],B[i] = map(int,input().split())

for i in range(n):
    C[i],D[i] = map(int,input().split())

def change(X):
    s = sum(X)
    for i in range(n):
        X[i] *= n
        X[i] -= s
    return X

A = change(A)
B = change(B)
C = change(C)
D = change(D)
for i in range(n):
    if A[i] or B[i]:
        A[i],A[0] = A[0],A[i]
        B[i],B[0] = B[0],B[i]

ans = "No"
eps = 10**(-6)
for i in range(n):
    angle = atan2(D[i],C[i])-atan2(B[0],A[0])
    ok = 1
    for j in range(n):
        a = A[j]*cos(angle)-B[j]*sin(angle)
        b = A[j]*sin(angle)+B[j]*cos(angle)
        ok2 = 0
        for k in range(n):
            if abs(a-C[k]) <= eps and abs(b-D[k]) <= eps:
                ok2 = 1
                break
        ok &= ok2
    if ok:
        ans = "Yes"
        break
print(ans)
