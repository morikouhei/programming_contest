import sys
sys.setrecursionlimit(2*10**5)
n = int(input())
mod = 10**9+7
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)


def dfs(x,p=-1):
    b = 1
    w = 1
    for nex in e[x]:
        if nex == p:
            continue
        nb,nw = dfs(nex,x)
        b *= nw
        b %= mod
        w *= (nb+nw)
        w %= mod
    return b,w

b,w = dfs(0)
print((b+w)%mod)