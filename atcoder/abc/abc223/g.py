from collections import deque
import sys
sys.setrecursionlimit(2*10**5)
n = int(input())
e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

topo = []
par = [-1]*n
q = deque([0])
while q:
    now = q.pop()
    topo.append(now)
    for nex in e[now]:
        if par[now] == nex:
            continue
        q.append(nex)
        par[nex] = now

match = [[0]*2 for i in range(n)]

for now in topo[::-1]:
    count = 0
    difs = 0
    for nex in e[now]:
        if par[now] == nex:
            continue
        count += match[nex][1]
        difs = max(difs,-match[nex][1]+match[nex][0]+1)

    match[now][0] = count
    match[now][1] = count+difs
    
ma = match[0][1]
ans = 0

def dfs(x,p,num0,num1):

    count = num1 + match[x][0]
    if count == ma:
        global ans
        ans += 1

    l = []
    if p == -1:
        l.append(0)
    else:
        l.append(-num1+num0+1)
    for nex in e[x]:
        if nex == p:
            continue
        l.append(max(l[-1],-match[nex][1]+match[nex][0]+1))

    r = []
    if p == -1:
        r.append(0)
    else:
        r.append(-num1+num0+1)
    for nex in e[x]:
        if nex == p:
            continue
        r.append(max(r[-1],-match[nex][1]+match[nex][0]+1))
    r = r[::-1]
    ind = 0
    for nex in e[x]:
        if nex == p:
            continue
        dfs(nex,x,count-match[nex][1],count+max(l[ind],r[ind+1])-match[nex][1])
        ind += 1

dfs(0,-1,0,0)
print(ans)
        