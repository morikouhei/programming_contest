import sys
sys.setrecursionlimit(3*10**5)
from collections import deque
n,m,k = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

visit = [0]*n
def dfs1(x,p):
    count = 0
    
    for nex in ne[x]:
        if nex == p:
            continue
        count += dfs1(nex,x)
    if count == 0:
        ans.append(x+1)
        return 1
    else:
        return 0


def dfs2(x,p,ans):
    if len(ans)> 1 and ans[0] == x+1:
        print(len(ans))
        print(*ans)
        exit()
    
    ans.append(x+1)
    for nex in ne[x]:
        if nex == p:
            continue
        dfs2(nex,x,ans)
    ans.pop()
    return 0

ne = [[] for i in range(n)]

s = set()
s.add(0)
q = deque([])
q.append((0,-1))
count = 1
f = True
while q and count < k and f:
    now,bef = q.popleft()
    for nex in e[now]:
        if bef == nex:
            continue
        if nex in s:
            continue
        count += 1
        check = 0
        s.add(nex)
        q.append((nex,now))
        for nex2 in e[nex]:
            if nex2 in s:
                ne[nex].append(nex2)
                ne[nex2].append(nex)
                check += 1
        if check > 1:
            f = False
            sta = nex
            
            break
if f:
    ans = []
    dfs1(0,-1)
    print(1)
    ans.sort()
    print(*ans[:(k+1)//2])

else:
    print(2)
    ans = []
    dfs2(sta,-1,ans)


