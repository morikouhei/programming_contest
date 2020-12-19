l = int(input())
dp = [[0]*(l+1) for i in range(12)]

dp[0][l] = 1

for i in range(11):
    for j in range(1,l+1):
        if dp[i][j]:
            for k in range(j):
                dp[i+1][k] += dp[i][j]
    
print(sum(dp[-1])-dp[-1][0])
