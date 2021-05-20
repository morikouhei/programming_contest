h,w = map(int,input().split())
A = [input() for i in range(h)]
dp = [[-10**10]*w for i in range(h)]
dp[-1][-1] = 0

for i in range(h)[::-1]:
    for j in range(w)[::-1]:
        if i == h-1 and j == w-1:
            continue
        if (i+j)%2 == 0:
            cand = -10**10
            num = 0
            if j != w-1:
                num = 1 if A[i][j+1] == "+" else -1
                cand = max(cand,dp[i][j+1]+num)
            if i != h-1:
                num = 1 if A[i+1][j] == "+" else -1
                cand = max(cand,dp[i+1][j]+num)
            dp[i][j] = cand
        else:
            cand = 10**10
            num = 0
            if j != w-1:
                num = 1 if A[i][j+1] == "+" else -1
                cand = min(cand,dp[i][j+1]-num)
            if i != h-1:
                num = 1 if A[i+1][j] == "+" else -1
                cand = min(cand,dp[i+1][j]-num)
            dp[i][j] = cand

if dp[0][0] == 0:
    print("Draw")
elif dp[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")