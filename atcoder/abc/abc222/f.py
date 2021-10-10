from collections import deque
import sys
sys.setrecursionlimit(5*10**5)
n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    a,b = a-1,b-1
    e[a].append((b,c))
    e[b].append((a,c))
D = list(map(int,input().split()))

topo = []
q = deque([0])
par = [-1]*n
while q:
    now = q.pop()
    topo.append(now)
    for nex,c in e[now]:
        if par[now] == nex:
            continue
        par[nex] = now
        q.append(nex)

E = [0]*n
for now in topo[::-1]:
    count = 0
    for nex,c in e[now]:
        if par[now] == nex:
            continue
        count = max(count,max(E[nex],D[nex])+c)
    E[now] = count

dp = [0]*n

def dfs(now,count,p=-1):
    cand0 = 0
    ind0 = -1
    cand1 = 0
    ind1 = -1
    for nex,c in e[now]:
        if nex == p:
            continue
        ncand = max(E[nex],D[nex])+c
        if ncand > cand0:
            cand1 = cand0
            ind1 = ind0
            cand0 = ncand
            ind0 = nex
        elif ncand > cand1:
            cand1 = ncand
            ind1 = nex

    dp[now] = max(E[now],count)
    count = max(count,D[now])
    if count > cand0:
        for nex,c in e[now]:
            if nex == p:
                continue
            dfs(nex,count+c,now)
    else:
        for nex,c in e[now]:
            if nex == p:
                continue
            if nex == ind0:
                dfs(nex,max(count,cand1)+c,now)
            else:
                dfs(nex,cand0+c,now)
dfs(0,0)
for i in dp:
    print(i)
