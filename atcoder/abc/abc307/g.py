n = int(input())
A = list(map(int,input().split()))

fa = sum(A)//n

inf = 10**20

dp = [inf]*n
dp[0] = 0
use = 0
for i,a in enumerate(A[:-1]):

    use += a
    ndp = [inf]*n
    for j in range(i+1):
        if dp[j] == inf:
            continue
        na = use - fa*(i-j) - (fa+1)*j
        ndp[j] = min(ndp[j],dp[j]+abs(na-fa))
        ndp[j+1] = min(ndp[j+1],dp[j]+abs(na-fa-1))
    dp = ndp

m = sum(A)%n

ans = dp[m]
if m:
    ans = min(ans,dp[m-1])

print(ans)