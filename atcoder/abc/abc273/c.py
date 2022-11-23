from collections import Counter
n = int(input())
A = list(map(int,input().split()))
C = Counter(A)

sA = sorted(set(A),reverse=True)

for i in range(len(sA)):
    print(C[sA[i]])
for i in range(n-len(sA)):
    print(0)