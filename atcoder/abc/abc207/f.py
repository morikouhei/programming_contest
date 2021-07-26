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
for now in topo[::-1]:
    dnow = [[0]*3 for i in range(2)]
    dnow[0][0] = 1
    dnow[1][2] = 1
    for nex in e[now]:
        if par[now] == nex:
            continue
        snow = len(dnow)
        snex = len(dp[nex])
        ndnow = [[0]*3 for i in range(snow+snex-1)]
        dnow,ndnow = ndnow,dnow
        for i in range(snow):
            for nowi in range(3):
                for j in range(snex):
                    for nexj in range(3):
                        val = ndnow[i][nowi]*dp[nex][j][nexj]
                        if val == 0:
                            continue
                        si = i+j
                        sj = -1
                        if nowi == 0 and nexj != 2:
                            sj = 0
                        elif nowi == 2:
                            sj = 2
                        else:
                            sj = 1
                        if nowi == 0 and nexj == 2:
                            si += 1
                        elif nowi == 2 and nexj == 0:
                            si += 1
                        dnow[si][sj] += val
                        dnow[si][sj] %= mod
    dp[now] = dnow

for i in range(n+1):
    print(sum(dp[0][i])%mod)