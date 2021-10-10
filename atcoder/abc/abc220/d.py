n = int(input())
A = list(map(int,input().split()))
mod = 998244353
dp = [0]*10
dp[A[0]] = 1
for a in A[1:]:
    ndp = [0]*10
    for i in range(10):
        ndp[(i+a)%10] += dp[i]
        ndp[(i+a)%10] %= mod
        ndp[(i*a)%10] += dp[i]
        ndp[(i*a)%10] %= mod
    dp = ndp
for i in dp:
    print(i)