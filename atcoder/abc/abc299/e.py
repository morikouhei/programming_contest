from collections import deque
n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)



black = [-1]*n

k = int(input())

def search(p,d):
    dist = [n+1]*n
    dist[p] = 0
    q = deque([p])
    while q:
        now = q.popleft()
        for nex in e[now]:
            nd = dist[now]+1
            if nd < dist[nex] and nd <= d:
                dist[nex] = nd
                q.append(nex)
    
    cands = []
    find = 0
    for i in range(n):
        if dist[i] < d:
            black[i] = 0
        elif dist[i] == d and black[i] == -1:
            cands.append(i)
            find = 1
    
    if find == 0:
        print("No")
        exit()

    return cands

cands = []
for _ in range(k):
    p,d = map(int,input().split())
    p -= 1

    cand = search(p,d)
    cands.append(cand)

black = [-x for x in black]

for cand in cands:
    find = 0
    for x in cand:
        if black[x]:
            find = 1
    
    if find == 0:
        print("No")
        exit()
print("Yes")
print(*black,sep="")
