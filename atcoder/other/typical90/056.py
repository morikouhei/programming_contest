n,s = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(n)]

dp = [[-1]*(s+1) for i in range(n+1)]
dp[0][0] = 0
for i,(a,b) in enumerate(AB):
    for j in range(s+1):
        if dp[i][j] == -1:
            continue
        if a+j <= s:
            dp[i+1][j+a] = 0
        if b+j <= s:
            dp[i+1][j+b] = 1

if dp[-1][-1] == -1:
    print("Impossible")
    exit()

ans = ["A"]*n
for i in range(n)[::-1]:
    a,b = AB[i]
    if dp[i+1][s] == 1:
        ans[i] = "B"
        s -= b
    else:
        s -= a

print(*ans,sep="")