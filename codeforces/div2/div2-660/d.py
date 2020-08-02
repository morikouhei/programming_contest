from collections import deque
import sys 
sys.setrecursionlimit(250000)
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

e = [[] for i in range(n)]
p = [0]*n
for i in range(n):
    x,y = a[i],b[i]
    y -= 1
    if y >= 0:
    
        e[i].append(y)
        p[y] += 1
        
        
q = deque([])
ans = 0
topo = []
topo2 = []
for i in range(n):
    if p[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    ans += a[now]
    if a[now] > 0:
        topo.append(now+1)
        if b[now] > 0:
            a[b[now]-1] += a[now]
    else:
        topo2.append(now+1)
    for nex in e[now]:
        if p[nex] > 0:
            p[nex] -= 1
        if p[nex] == 0:
            q.append(nex)
print(ans)
print(*topo,end=" ")
print(*topo2[::-1])