import sys
sys.setrecursionlimit(2*10**5)

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    e[a-1].append(b-1)
def dfs(x):
    num = 0
    for nex in e[x]:
        if dis[nex] < 0:
            dfs(nex)
        num = max(num,dis[nex]+1)
    dis[x] = num
    return 
dis = [-1]*n
for i in range(n):
    if dis[i] < 0:
        dfs(i)
print(max(dis))