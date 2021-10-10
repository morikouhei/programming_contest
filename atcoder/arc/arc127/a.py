n = input()
ans = 0
dp = [[0]*2 for i in range(10)]

s = int(n[0])
if s == 1:
    dp[1][1] = 1
else:
    dp[1][0] = 1
print(dp)

if s == 1:
    first = 1
    upd = 0
else:
    first = 0
    upd = 1
for s in n[1:]:
    s = int(s)
    ndp = [[0]*2 for i in range(10)]
    ndp[1][0] += 1
    for i in range(10):
        for j in range(10):
            if j > s:
                ndp[j][0] += dp[i][0]
                continue
            if j < s:
                ndp[j][0] += dp[i][0]+dp[i][1]
            elif j == s:
                ndp[j][1] += dp[i][1]
                ndp[j][0] += dp[i][0]

            
    if s > 1:
        if first:
            first = 0
        ndp[1][0] += upd+first
    elif s == 1:
        if first:
            ndp[1][1] += upd+first
        else:
            ndp[1][0] += upd+first
    else:
        if first:
            first = 0
        ndp[1][0] += upd
    upd += 1
    dp = ndp
    print(dp,upd)
ans = 0
for i in dp:
    ans += sum(i)
print(ans)
