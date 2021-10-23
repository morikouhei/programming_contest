from heapq import heappush, heappop
n,m = map(int,input().split())
e = [[] for i in range(n)]
count = [0]*n
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    count[b] += 1

ans = []
h = []
for i in range(n):
    if count[i]:
        continue
    heappush(h,i)

while h:
    now = heappop(h)
    ans.append(now+1)
    for nex in e[now]:
        count[nex] -= 1
        if count[nex] == 0:
            heappush(h,nex)
if len(ans) == n:
    print(*ans)
else:
    print(-1)

