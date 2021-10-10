n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
mod = 998244353
M = 3005
dp = [1]*M


for i in range(n):
    a = A[i]
    b = B[i]
    ndp = [0]*M
    for j in range(M):
        if a <= j <= b:
            ndp[j] += dp[j]
            ndp[j] %= mod
        ndp[j] += ndp[j-1]
        ndp[j] %= mod
    dp = ndp

print(dp[-1])