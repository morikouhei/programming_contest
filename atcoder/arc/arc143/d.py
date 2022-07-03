import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
e = [[] for i in range(n)]
A = list(map(int,input().split()))
B = list(map(int,input().split()))

for i,(a,b) in enumerate(zip(A,B)):
    a -= 1
    b -= 1
    e[a].append([b,i,0])
    e[b].append([a,i,1])


vis = [0]*n
ans = [-1]*m

def dfs(x):
    
    if vis[x]:
        return
    vis[x] = 1

    for nex,ind,d in e[x]:
        if ans[ind] != -1:
            continue

        ans[ind] = d
        if vis[nex]:
            continue
        dfs(nex)

for i in range(n):
    if vis[i]:
        continue
    dfs(i)

print(*ans,sep="")