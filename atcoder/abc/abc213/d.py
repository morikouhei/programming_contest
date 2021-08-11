import sys
sys.setrecursionlimit(4*10**5)
n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
for i in range(n):
    e[i].sort()

ans = []
vis = [0]*n

def dfs(now,bef=-1):
    ans.append(now+1)
    vis[now] = 1
    for nex in e[now]:
        if vis[nex]:
            continue
        dfs(nex,now)
        ans.append(now+1)
    return

dfs(0)
print(*ans)