from heapq import heappop,heappush
n = int(input())
PTSG = [list(map(int,input().split())) for i in range(n-1)]
child = [[] for i in range(n)]
med = 0
meds = []
max_strength = 0
for i,(p,t,s,g) in enumerate(PTSG,1):
    max_strength = max(max_strength,s)
    child[p-1].append(i)
    if t == 2:
        med += 1
        meds.append(i)


dp = [0]*(1<<med)
dp[0] = 1

memo = [[] for i in range(1<<med)]
vis = [0]*n
vis[0] = 1
def update(vis,strength):
    nvis = [v for v in vis]

    h = []
    for ind,(p,t,s,g) in enumerate(PTSG,1):
        if nvis[ind]:
            continue
        if t == 2:
            continue
        if nvis[p-1] == 0:
            continue

        
        heappush(h,[s,ind])

    
    while h:
        s,ind = heappop(h)
        if nvis[ind]:
            continue

        if strength >= s:
            nvis[ind] = 1
            strength += PTSG[ind-1][3]

            for nex in child[ind]:
                if PTSG[nex-1][1] == 1:
                    heappush(h,[PTSG[nex-1][2],nex])

    return nvis,strength


vis,strength = update(vis,dp[0])
dp[0] = strength
memo[0] = vis

for i in range(1<<med):
    if dp[i] == 0:
        continue

    vis = memo[i]
    for j,ind in enumerate(meds):
        if vis[ind]:
            continue
        p,t,s,g = PTSG[ind-1]
        p -= 1
        if vis[p] == 0:
            continue

        strength = dp[i] * g

        vis[ind] = 1
        nvis,strength = update(vis,strength)

        ni = i | 1 << j
        if dp[ni] < strength:
            dp[ni] = strength
            memo[ni] = nvis
        
        vis[ind] = 0

print("Yes" if max(dp) >= max_strength else "No")