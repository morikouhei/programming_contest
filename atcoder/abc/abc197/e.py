n = int(input())
l = [list(map(int,input().split())) for i in range(n)]

L = [10**10]*(n+1)
R = [-10**10]*(n+1)
for x,c in l:
    L[c] = min(L[c],x)
    R[c] = max(R[c],x)


L[0] = 0
R[0] = 0

now = 0
dp = [0]*2
print(L,R)
for i in range(n+1):
    if L[i] == 10**10:
        continue
    candl = 10**20
    if R[i] <= L[now]:
        cal1 = L[now]-L[i]+dp[0]
    else:
        cal1 = max(0,R[i]-L[now])+R[i]-L[i]+dp[0]

    if R[i] <= R[now]:
        cal2 = R[now]-L[i]+dp[1]
    else:
        cal2 = max(0,R[i]-R[now])+R[i]-L[i]+dp[1]
    candl = min(cal1,cal2)

    candr = 10**20
    if L[i] >=  L[now]:
        cal1 = R[i]-L[now]+dp[0]
    else:
        cal1 = max(0,L[now]-L[i])+R[i]-L[i]+dp[0]

    if L[i] >= R[now]:
        cal2 = R[i]-R[now]+dp[1]
    else:
        cal2 = max(0,R[now]-L[i])+R[i]-L[i]+dp[1]
    candr = min(cal1,cal2)
    dp = [candl,candr]
    now = i
ans = dp[0]+abs(L[now])
ans = min(ans,dp[1]+abs(R[now]))
print(ans)