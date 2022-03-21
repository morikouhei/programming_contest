n,m,k,s,t,x = map(int,input().split())
mod = 998244353
edges = [[int(j)-1 for j in input().split()] for i in range(m)]
s -= 1
t -= 1
x -= 1


dp0 = [0]*n
dp1 = [0]*n

dp0[s] = 1

for i in range(k):
    ndp0 = [0]*n
    ndp1 = [0]*n
    for u,v in edges:
        if v == x:
            ndp1[v] += dp0[u]
            ndp0[v] += dp1[u]
        else:
            ndp0[v] += dp0[u]
            ndp1[v] += dp1[u]

        if u == x:
            ndp1[u] += dp0[v]
            ndp0[u] += dp1[v]
        else:
            ndp0[u] += dp0[v]
            ndp1[u] += dp1[v]
        ndp0[u] %= mod
        ndp0[v] %= mod
        ndp1[u] %= mod
        ndp1[v] %= mod
    dp0 = ndp0
    dp1 = ndp1
print(dp0[t])
