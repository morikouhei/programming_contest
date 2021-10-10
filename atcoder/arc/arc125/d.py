n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dic = {}

cum = 1
dp = [0]*(n+1)
dp[0] = 1
for i,a in enumerate(A,1):
    if a in dic:
        dp[i] = cum-dp[dic[a]-1]
        dp[i] %= mod
        cum -= dp[dic[a]]
        cum %= mod
    else:
        dp[i] = cum
    dic[a] = i
    cum += dp[i]
    cum %= mod

ans = 0
for v in dic.values():
    ans += dp[v]
    ans %= mod
print(ans)