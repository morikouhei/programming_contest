n = int(input())
a = list(map(int,input().split()))

ans = 0
dp = [0]*(n+2)
sa = [[a[i],i+1] for i in range(n)]
sa.sort(reverse=True)
for a,i in sa:
    r = i+dp[i+1]
    l = i-dp[i-1]
    dp[l] = dp[r] = dp[i] = r-l+1
    ans = max(ans,a*dp[i])

print(ans)
