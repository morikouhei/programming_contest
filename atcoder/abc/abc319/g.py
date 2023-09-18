from collections import deque

n,m = map(int,input().split())
mod = 998244353
UV = [[int(x)-1 for x in input().split()] for i in range(m)]

ban_set = [set() for i in range(n)]
for u,v in UV:
    ban_set[u].add(v)
    ban_set[v].add(u)

rest = set([i for i in range(1,n)])
dist = [n]*n
now = [0]
dist[0] = 0
dp = [0]*n
dp[0] = 1
while now:

    if n-1 in now:
        break
    
    nex = set()
    for i in now:
        d = dist[i]
        rem = []
        for cand in rest:
            if cand in ban_set[i]:
                continue

            if dist[cand] > d+1:
                nex.add(cand)
                rem.append(cand)
                dist[cand] = d+1

        for r in rem:
            rest.remove(r)

    count = 0
    for i in now:
        count += dp[i]
        count %= mod

    for i in nex:
        dp[i] = count

    for i in now:
        for ni in ban_set[i]:
            if ni in nex:
                dp[ni] -= dp[i]
                dp[ni] %= mod    

    now = nex

ans = dp[-1] if dist[-1] < n else -1
print(ans)

