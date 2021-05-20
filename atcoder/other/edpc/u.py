n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

inf = 10**20
dp = [-inf]*(1<<n)
for i in range(1<<n):
    count = 0
    for j in range(n):
        if i >> j & 1:
            for k in range(j):
                if i >> k & 1:
                    count += A[j][k]
    dp[i] = count

for i in range(1<<n):
    now = i&(i-1)
    while now:
        dp[i] = max(dp[i],dp[now]+dp[i^now])
        now = (now-1)&i
print(dp[-1])
