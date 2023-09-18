n = int(input())
D = [[0]*n for i in range(n)]
for i in range(n-1):
    d = list(map(int,input().split()))
    for j in range(i+1,n):
        D[i][j] = D[j][i] = d[j-i-1]


dp = [0]*(1<<n)

for b in range(1<<n):

    for i in range(n):
        if b >> i & 1:
            continue

        for j in range(i+1,n):
            if b >> j & 1:
                continue
            nb = b | (1<<i) | (1<<j)
            dp[nb] = max(dp[nb],dp[b]+D[i][j])
print(max(dp))