from collections import deque
n,q = map(int,input().split())

e = [[] for i in range(n+1)]
for i in range(q):
    l,r = map(int,input().split())
    e[l-1].append(r)
    e[r].append(l-1)

use = [0]*(n+1)
use[0] = 1
q = deque([0])
while q:
    now = q.popleft()
    for nex in e[now]:
        if use[nex]:
            continue
        use[nex] = 1
        q.append(nex)

print("Yes" if use[-1] else "No")