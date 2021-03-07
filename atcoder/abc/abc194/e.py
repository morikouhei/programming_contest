from heapq import heappush, heappop
n,m = map(int,input().split())
A = list(map(int,input().split()))

l = [0]*(n+5)
for i in range(m):
    l[A[i]] += 1

for i in range(n+2):
    if l[i] == 0:
        mex = i
        break
ans = mex
h = []
for i in range(m,n):
    l[A[i-m]] -= 1
    l[A[i]] += 1
    if l[A[i-m]] == 0 and mex > A[i-m]:
        if l[mex] == 0:
            heappush(h,mex)
        mex = A[i-m]
        ans = min(ans,mex)
        continue
    if l[mex] >= 0:
        M = mex
        while h:
            cand = heappop(h)
            M = max(M,cand)
            if l[cand] == 0:
                mex = cand
                break
        if l[mex] == 0:
            continue
        for j in range(M,n+2):
            if l[j] == 0:
                mex = j
                break
    ans = min(ans,mex)
print(ans)

