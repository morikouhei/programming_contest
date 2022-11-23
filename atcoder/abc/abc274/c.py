from collections import deque
n = int(input())
A = list(map(int,input().split()))

e = [[] for i in range(2*n+2)]

for i,a in enumerate(A,1):
    e[a].append(2*i)
    e[a].append(2*i+1)

dist = [10**10]*(2*n+2)
dist[1] = 0
q = deque([1])
while q:
    now = q.popleft()
    for nex in e[now]:
        if dist[nex] > dist[now]+1:
            dist[nex] = dist[now]+1
            q.append(nex)

for i in dist[1:]:
    print(i)