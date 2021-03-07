S = input()
T = input()
ls,lt = len(S)+1,len(T)+1

dp = [[0]*lt for i in range(ls)]
for i,s in enumerate(S):
    for j,t in enumerate(T):
        dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1],dp[i][j]+(s==t))

ans = ""
x = ls-1
y = lt-1
while x and y:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        x -= 1
        y -= 1
        ans = S[x]+ans
print(ans)