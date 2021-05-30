from collections import deque
import sys
input = sys.stdin.buffer.readline
      
t = int(input())
for _ in range(t):
    q = input()
    n,m = map(int,input().split())
    e = [[] for i in range(n)]
    for i in range(m):
        u,v = map(int,input().split())
        e[u-1].append(v-1)

    dis = [n]*n
    q = deque([0])
    dis[0] = 0
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] > dis[now]+1:
                dis[nex] = dis[now]+1
                q.append(nex)
    dist = [[] for i in range(n)]
    for i,x in enumerate(dis):
        dist[x].append(i)
    ans = [n]*n
    for i in range(n)[::-1]:
        for now in dist[i]:
            cand = dis[now]
            for nex in e[now]:
                if dis[nex] > dis[now]:
                    if cand > ans[nex]:
                        cand = ans[nex]
                else:
                    if cand > dis[nex]: 
                        cand = dis[nex]
            ans[now] = cand
    print(*ans)