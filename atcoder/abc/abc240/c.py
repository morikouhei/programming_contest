n,x = map(int,input().split())
dp = [0]*(x+5)
dp[0] = 1
for i in range(n):
    a,b = map(int,input().split())
    ndp = [0]*(x+5)
    for j in range(x+1)[::-1]:
        if dp[j]:
            if j + a <= x:
                ndp[j+a] = 1
            if j+b <= x:
                ndp[j+b] = 1
    dp = ndp
print("Yes" if dp[x] else "No")
