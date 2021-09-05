n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB = [[a,b] for a,b in zip(A,B)]
AB.sort(key=lambda x: -x[0])
mod = 998244353
M = 5005
dp = [0]*M

for a,b in AB:
    for i in range(M):
        if dp[i] == 0:
            continue
        if i-b >= 0:
            dp[i-b] += dp[i]
            dp[i-b] %= mod

    if a >= b:
        dp[a-b] += 1
print(sum(dp)%mod)