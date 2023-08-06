import sys
input = sys.stdin.readline
sys.setrecursionlimit(3*10**5)
n = int(input())
A = list(map(int,input().split()))
e = [[] for i in range(n+1)]
for i,a in enumerate(A,1):
    e[i].append(a)


vis = [-1]*(n+1)
par = [-1]*(n+1)
def dfs(x,p,id):
    for nex in e[x]:
        if vis[nex] == id:

            ans = [x]
            while nex != x:
                x = par[x]
                ans.append(x)
            print(len(ans))
            print(*ans[::-1])
            exit()
        elif vis[nex] != -1:
            continue

        vis[nex] = id
        par[nex] = x
        dfs(nex,x,id)


for i in range(1,n+1):
    if vis[i] != -1:
        continue
    vis[i] = i

    dfs(i,-1,i)
