from collections import deque

n,m = map(int,input().split())
e = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    e[a].append(b)
    e[b].append(a)

vis = [-1]*(n+1)
Q = int(input())
for t in range(Q):
    x,k = map(int,input().split())

    q = deque([[x,k]])
    vis[x] = t
    ans = 0
    while q:
        now,left = q.popleft()
        ans += now
        if left == 0:
            continue

        for nex in e[now]:
            if vis[nex] == t:
                continue
            vis[nex] = t
            q.append([nex,left-1])
    print(ans)