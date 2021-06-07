import sys
input = sys.stdin.buffer.readline

n,m,q = map(int,input().split())

XY = [[int(x)-1 for x in input().split()] for i in range(m)]
XY.sort(key=lambda x: (x[1],x[0]))

A = []
B = []
for i in range(q):
    a,b = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
K = (q+15)//16
ans = [0]*q
for i in range((q+K-1)//K):
    dp = [0]*n
    for j in range(K):
        if i*K+j < q:
            dp[A[i*K+j]] |= 1<<j
    for x,y in XY:
        dp[y] |= dp[x]
    for j in range(K):
        if i*K+j < q:
            if dp[B[i*K+j]] >> j & 1:
                ans[i*K+j] = 1
for i in ans:
    print("Yes" if i else "No")
