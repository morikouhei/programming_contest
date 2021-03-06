import sys
sys.setrecursionlimit(2*10**5)
n = int(input())
C = input().split(" ")
mod = 10**9+7
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)

dp = [[-1]*3 for i in range(n)]
def dfs(x,p=-1):
    if dp[x][0] != -1:
        return dp[x]
    
    
    id = int(C[x] == "b")
    dpx = [0]*3
    dpx[id] = 1
    dpx[2] = 1
    for nex in e[x]:
        if nex == p:
            continue
        ndp = dfs(nex,x)
        dpx[id] *= (ndp[id]+ndp[2])
        dpx[id] %= mod
        dpx[2] *= sum(ndp)+ndp[2]
        dpx[2] %= mod
    dpx[2] -= dpx[id]
    dpx[2] %= mod
    dp[x] = dpx
    return dpx

dfs(0)
print(dp[0][2])