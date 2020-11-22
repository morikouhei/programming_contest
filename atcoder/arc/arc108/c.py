import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())
e = [[] for i in range(n+1)]
s = [set() for i in range(n+1)]
for i in range(m):
    u,v,c = map(int,input().split())

    e[u].append((v,c))
    e[v].append((u,c))

ans = [0]*(n+1)
q = deque([[1,0]])
ans[1] = e[1][0][1]
while q:
    now, bef = q.popleft()
    for nex,c in e[now]:
        if nex == bef:
            continue
        s[nex].add(ans[now])
        if ans[nex] > 0:
            continue
        if ans[now] != c:
            ans[nex] = c
            q.append([nex,now])
        else:
            check = False
            for _,c in e[nex]:
                if c not in s[nex]:
                    check = True
                    ans[nex] = c
                    break
            if check == False:
                for j in range(1,n+1):
                    if j not in s[nex]:
                        ans[nex] = j
                        break
            q.append([nex,now])

for i in ans[1:]:
    print(i)
