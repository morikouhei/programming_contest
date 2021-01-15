import sys
sys.setrecursionlimit(10**6)
n = int(input())
M = 4*10**5+1
e = [[] for i in range(M)]
for i in range(n):
    a,b = map(int,input().split())
    e[a].append(b)
    e[b].append(a)

ans = 0
used = [0]*(M)

def dfs(x,p):
    size = 1
    tree = 0
    used[x] = 1
    for i in e[x]:
        if i == p:
            continue
        if used[i]:
            tree = 1
            continue
        s, t = dfs(i,x)
        size += s
        tree = max(tree,t)

    return size,tree

for i in range(1,M):
    if used[i] or e[i] == []:
        continue
    size,tree = dfs(i,-1)

    if tree:
        ans += size
    else:
        ans += size-1

print(ans)