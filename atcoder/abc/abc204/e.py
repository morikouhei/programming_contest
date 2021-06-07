from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b,c,d = [int(x) for x in input().split()]
    e[a-1].append((b-1,c,d))
    e[b-1].append((a-1,c,d))

inf = 10**20
mod = 1<<32

def search(c,d,t):
    if t > int(d**0.5)+1:
        return t+c+d//(t+1)

    ans = inf
    for i in range(int(d**0.5)-5,int(d**0.5)+5):
        if i < t:
            continue
        ans = min(ans,i+c+d//(i+1))
    
    return ans



dis = [inf]*n
dis[0] = 0
h = [0]
while h:
    d,now = divmod(heappop(h),mod)
    if dis[now] != d:
        continue
    for nex,nc,nd in e[now]:
        best = search(nc,nd,d)
        if dis[nex] > best:
            dis[nex] = best
            heappush(h,(best<<32)+nex)
ans = dis[-1]
if ans == inf:
    ans = -1
print(ans)

