n = int(input())
P = list(map(int,input().split()))

inf = 10**10
dp = [-inf]*(n+1)
dp[0] = 0
for p in P:

    for i in range(n)[::-1]:
        if dp[i] == -inf:
            continue
        dp[i+1] = max(dp[i+1],dp[i]*0.9 + p)

ans = -10**10

inv = 0
inv9 = 1
for i in range(1,n+1):

    inv += inv9
    inv9 *= 0.9

    rate = dp[i] / inv - 1200/(i**0.5)
    ans = max(ans,rate)
print(ans)
