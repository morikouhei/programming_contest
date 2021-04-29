from collections import deque

n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

dis = [-1]*n
q = deque([0])
dis[0] = 0
while q:
    now = q.popleft()
    for nex in e[now]:
        if dis[nex] == -1:
            dis[nex] = dis[now]^1
            q.append(nex)
        
ok = 1 if sum(dis)*2 >= n else 0
ans = []
for i in range(n):
    if dis[i] == ok:
        ans.append(i+1)
print(*ans[:n//2])