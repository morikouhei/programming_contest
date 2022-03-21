import sys
input = sys.stdin.readline
from math import ceil, sqrt

n = int(input())
A = list(map(int,input().split()))
q = int(input())
LR = [list(map(int,input().split())) for i in range(q)]

sq = int(ceil(sqrt(q)))
Query = [[] for i in range(sq)]
for i,(l,r) in enumerate(LR):
    l -= 1
    Query[l*sq//n].append([l,r,i])
for i in range(sq):
    if i&1:
        Query[i].sort(key=lambda x:-x[1])
    else:
        Query[i].sort(key=lambda x:x[1])

ans = [0]*q

num = [0]*(n+1)

count = 0
nl = -1
nr = 0
for Q in Query:
    for l,r,ind in Q:
        l -= 1
        while nr < r:
            x = A[nr]
            num[x] += 1
            if not num[x]&1:
                count += 1
            nr += 1
        while nr > r:
            nr -= 1
            x = A[nr]
            num[x] -= 1
            if num[x]&1:
                count -= 1

        while l < nl:
            x = A[nl]
            num[x] += 1
            if not num[x]&1:
                count += 1
            nl -= 1

        while l > nl:
            nl += 1
            x = A[nl]
            num[x] -= 1
            if num[x]&1:
                count -= 1

        ans[ind] = count

for i in ans:
    print(i)

