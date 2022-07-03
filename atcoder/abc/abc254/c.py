n,k = map(int,input().split())
A = list(map(int,input().split()))
L = [[] for i in range(k)]
for i,a in enumerate(A):
    L[i%k].append(a)

nA = [0]*n
for i in range(k):
    L[i].sort()
    for j in range(len(L[i])):
        nA[i+k*j] = L[i][j]

print("Yes" if sorted(A) == nA else "No")