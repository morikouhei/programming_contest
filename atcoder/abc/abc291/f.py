n,m = map(int,input().split())
S = [list(map(int,input())) for i in range(n)]

inf = 10**10
dp0 = [inf]*n
dp0[0] = 0

for i,s in enumerate(S):
    if dp0[i] == inf:
        continue
    for j in range(m):
        if s[j] == 0:
            continue
        if i+j+1 < n:
            dp0[i+j+1] = min(dp0[i+j+1],dp0[i]+1)

# print(dp0)
dpn = [inf]*n
dpn[-1] = 0
for i in range(n-1)[::-1]:
    s = S[i]
    for j in range(m):
        if s[j] == 0:
            continue
        if i+j+1 < n:
            dpn[i] = min(dpn[i],dpn[i+j+1]+1)

# print(dpn)
ans = []
for i in range(1,n-1):
    dis = inf
    for j in range(max(0,i-m),i):
        if dp0[j] == inf:
            continue
        s = S[j]
        for k in range(m):
            if i < j+k+1 < n and s[k]:
                dis = min(dis,dp0[j]+dpn[j+k+1]+1)
    if dis == inf:
        dis = -1
    ans.append(dis)
print(*ans)