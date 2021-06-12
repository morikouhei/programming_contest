from collections import deque
n = int(input())
AB = [[x-1 for x in map(int,input().split())] for i in range(n)]
use = [0]*n
q = deque([])
e = [[] for i in range(n)]
for i, (a,b) in enumerate(AB):
    if a == i or b == i:
        use[i] = 1
        q.append(i)
    e[a].append(i)
    e[b].append(i)
ans = []
while q:
    now = q.popleft()
    ans.append(now+1)
    for nex in e[now]:
        if use[nex]:
            continue
        q.append(nex)
        use[nex] = 1

if len(ans) != n:
    ans = [-1]

for i in ans[::-1]:
    print(i)