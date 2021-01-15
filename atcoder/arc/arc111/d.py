n,m = map(int,input().split())
e = [[] for i in range(n)]
edge = [[int(i)-1 for i in input().split()] for j in range(m)]
c = list(map(int,input().split()))

ans = [-1]*m
for i,(a,b) in enumerate(edge):
    if c[a] == c[b]:
        e[a].append((b,i))
        e[b].append((a,i))
        continue

    ans[i] = c[a] < c[b]
    
use = [0]*n
def dfs(x):
    if use[x]:
        return
    use[x] = 1

    for nex,ind in e[x]:
        if ans[ind] >= 0:
            continue
        ans[ind] = edge[ind][0] == nex
        dfs(nex) 
    
for i in range(n):
    dfs(i)

for i in ans:
    print("<-" if i else "->")