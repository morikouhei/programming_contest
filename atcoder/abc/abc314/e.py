n,m = map(int,input().split())

inf = 10**10
dp = [inf]*(2*m+1)

dp[0] = 0

CPS = [list(map(int,input().split())) for i in range(n)]

for i in range(1,2*m+1):


    for j in range(n):
        c = CPS[j][0]
        p = CPS[j][1]
        s = CPS[j][2:]
        
        count = 0
        zero = 0
        for x in s:
            if x == 0:
                zero += 1
                continue

            if i-x >= 0:
                count += dp[i-x]
            else:
                count += 0

        dp[i] = min(dp[i],(c+count/p)*p/(p-zero))

ans = min(dp[m:])
print(ans)
