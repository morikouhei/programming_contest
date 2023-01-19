import sys
sys.setrecursionlimit(2*10**7)
n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

vis = [0]*n

ans = 0

def dfs(x):
    global ans
    ans += 1
    if ans >= 10**6:
        print(10**6)
        exit()

    vis[x] = 1
    for nex in e[x]:
        if vis[nex]:
            continue
        dfs(nex)
    
    vis[x] = 0
    return

dfs(0)
print(ans)
    