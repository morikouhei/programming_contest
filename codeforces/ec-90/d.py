t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    if n%2:
        l.append(0)
    
    dp = [[0]*4 for i in range((n+1)//2+1)]
    for i in range((n+1)//2):
        dp[i+1][0] = dp[i][0]+l[i*2]
        dp[i+1][1] = max(dp[i][1],dp[i][0])
        if i >= 1:
            dp[i+1][1] += l[i*2-1]
        dp[i+1][2] = max(dp[i][0],dp[i][2])+l[i*2+1]
        
        dp[i+1][3] = max(dp[i][3],dp[i][1],dp[i][2])+l[i*2]
    print(max(dp[-1]))
    