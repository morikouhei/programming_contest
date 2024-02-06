n,k,p = map(int,input().split())
M = 6**5
inf = 10**15
dp = [inf]*M
dp[0] = 0

for _ in range(n):
    c,*A = map(int,input().split())

    for i in range(M)[::-1]:
        if dp[i] == inf:
            continue
        ids = []
        id = i
        for j in range(k):
            ids.append(id%6)
            id //= 6
        for j in range(k):
            ids[j] = min(p,ids[j]+A[j])
        id = 0
        for j in range(k)[::-1]:
            id *= 6
            id += ids[j]
        
        if dp[id] > dp[i]+c:
            dp[id] = dp[i]+c


ans = inf
for i in range(M):
    ids = []
    id = i
    for j in range(k):
        ids.append(id%6)
        id //= 6
    
    if min(ids) >= p:
        ans = min(ans,dp[i])
if ans == inf:
    ans = -1
print(ans)

