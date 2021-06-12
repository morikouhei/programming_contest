from collections import deque

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

dis = [n]*n
par = [-1]*n
q = deque([0])
dis[0] = 0
while q:
    now = q.popleft()
    for nex in e[now]:
        if dis[nex] > dis[now]+1:
            q.append(nex)
            dis[nex] = dis[now]+1
            par[nex] = now

def solve():
    Q = [int(x)-1 for x in input().split()]
    cand = []
    dic = {}
    id = {}
    for i in Q[1:]:
        p = par[i]
        if p < 1:
            continue
        if dis[p] in dic:
            print("NO")
            return
        dic[p] = 1
        id[p] = 1
        cand.append(p)
    if cand == []:
        print("YES")
        return
    
    dep = 0
    ind = -1
    for i in cand:
        if dep < dis[i]:
            dep = dis[i]
            ind = i
    
    while ind != 0:
        if ind in id:
            id[ind] = 0
        ind = par[ind]
    for i in id.keys():
        if id[i]:
            print("NO")
            return
    print("YES")
    
    
for _ in range(m):
    solve()