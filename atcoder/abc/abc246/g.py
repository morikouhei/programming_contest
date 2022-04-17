from collections import deque

n = int(input())
A = [0]+list(map(int,input().split()))
e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)
topo = []
vis = [0]*n
vis[0] = 1
par = [-1]*n
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        par[nex] = now
        q.append(nex)

    
def solve(x):
    dp = [0]*n
    for now in topo[::-1]:
        turn = 0
        for nex in e[now]:
            if par[now] == nex:
                continue
            turn += dp[nex]
        turn -= 1
        dp[now] = max(0,turn) + int(A[now] >= x)
    return dp[0] > 0

l = 0
r = 10**10
while r > l + 1:
    m = (r+l)//2
    if solve(m):
        l = m
    else:
        r = m

print(l)