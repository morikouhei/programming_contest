from collections import deque
n = int(input())
mod = 10**9+7
e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

topo = []
par = [-1]*n
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        par[nex] = now
        q.append(nex)

dp = [-1]*n
size = [0]*n
print(topo)
for now in topo[::-1]:
    size[now] += 1
    dpnow = [[[0]*(n+1) for i in range(3)] for j in range(2)]
    dpnow[0][2][1] = 1
    dpnow[0][0][0] = 1
    dpnow[0][1][0] = 1
    turn = 0
    for nex in e[now]:
        if par[now] == nex:
            continue

        for i in range(size[now]+size[nex]+1)[::-1]:
            for j in range(min(size[nex],i)+1)[::-1]:
                if i-j > size[now]:
                    break
                dpnow[turn^1][0][i] += (dp[nex][0][j]+dp[nex][1][j])*dpnow[turn][0][i-j]
                dpnow[turn^1][0][i] %= mod
                dpnow[turn^1][2][i] += (dp[nex][0][j]+dp[nex][1][j]+dp[nex][2][j])*dpnow[turn][2][i-j]
                dpnow[turn^1][2][i] %= mod
                dpnow[turn^1][1][i] += (dp[nex][0][j]+dp[nex][1][j]+dp[nex][2][j])*dpnow[turn][1][i-j]
                dpnow[turn^1][1][i] %= mod
                turn ^= 1
        size[now] += size[nex]

    for i in range(size[now]+1):
        dpnow[turn][1][i] -= dpnow[turn][0][i]
        dpnow[turn][1][i] %= mod
    dp[now] = dpnow[turn]
print(dp)
for i in range(n+1):
    print((dp[0][0][i]+dp[0][1][i]+dp[0][2][i])%mod)


