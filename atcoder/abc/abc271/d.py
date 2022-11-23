n,s = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]

dp = [[-1]*(s+1) for i in range(n+1)]
dp[0][0] = 0

for i,(a,b) in enumerate(AB):
    for j in range(s+1):
        if dp[i][j] < 0:
            continue
        if j+a <= s:
            dp[i+1][j+a] = j
        if j+b <= s:
            dp[i+1][j+b] = j


if dp[-1][s] < 0:
    print("No")
    exit()

print("Yes")

now = s
ans = []
for i in range(n)[::-1]:
    nex = dp[i+1][now]
    dif = now-nex
    a,b = AB[i]
    if dif == a:
        ans.append("H")
    else:
        ans.append("T")
    now = nex
print(*ans[::-1],sep="")