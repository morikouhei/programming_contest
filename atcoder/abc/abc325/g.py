S = input()
k = int(input())
n = len(S)

dp = [[n]*(n+1) for i in range(n+1)]
for le in range(n+1):

    for l in range(n+1):

        r = l+le
        if r > n:
            break

        dp[l][r] = le

        for j in range(l,r):
            dp[l][r] = min(dp[l][r],dp[l][j] + dp[j][r])

        if l >= n or S[l] != "o":
            continue


        for j in range(l+1,r):
            if S[j] == "f" and dp[l+1][j] == 0 and dp[j+1][r] <= k:
                dp[l][r] = 0
                
        

print(dp[0][n])