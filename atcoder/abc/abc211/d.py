from collections import Counter, deque

n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    e[b].append(a)

mod = 10**9+7
dis = [n]*n
count = [0]*n
count[0] = 1
dis[0] = 0
q = deque([0])
while q:
    now = q.popleft()
    d = count[now]

    for nex in e[now]:
        if dis[nex] >  dis[now]+1:    
            dis[nex] = dis[now]+1
            count[nex] = d
            count[nex] %= mod
            q.append(nex)
        
        elif dis[nex] ==  dis[now]+1:    
            count[nex] += d
            count[nex] %= mod
        

print(count[-1])
    