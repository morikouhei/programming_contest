n,p,q,r,s = map(int,input().split())
A = list(map(int,input().split()))
p -= 1
r -= 1
x = A[p:q]
y = A[r:s]
B = A[:]
B[p:q] = y
B[r:s] = x
print(*B)