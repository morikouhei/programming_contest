from collections import deque
inf = 10**6+5
def solve():
    n,m = map(int,input().split())
    C = list(map(int,input().split()))

    e = [[] for i in range(n)]
    for i in range(m):
        u,v = [int(x)-1 for x in input().split()]
        e[u].append(v)
        e[v].append(u)

    dis = [inf]*(n**2)
    dis[n-1] = 0

    q = deque()
    q.append(n-1)
    while q:
        now = q.popleft()
        x,y = divmod(now,n)
        d = dis[now]
        for nx in e[x]:
            for ny in e[y]:
                if C[nx] == C[ny]:
                    continue
                nex = nx*n+ny
                if dis[nex] > d+1:
                    dis[nex] = d+1
                    q.append(nex)
            
    
    ans = dis[n*(n-1)]
    if ans == inf:
        ans = -1
    return ans


t = int(input())
for _ in range(t):
    print(solve())