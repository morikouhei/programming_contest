n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v,b,c = map(int,input().split())
    u,v = u-1,v-1

    e[u].append([v,b,c])

inf = 1e10
def solve(mid):

    dp = [-inf]*n
    dp[0] = 0

    for u in range(n):
        for v,b,c in e[u]:
            dp[v] = max(dp[v],dp[u] + b - c * mid)

    
    return dp[-1] >= 0

l = 0
r = 10**4

for i in range(50):

    mid = (l+r)/2

    if solve(mid):
        l = mid
    else:
        r = mid

print(l)