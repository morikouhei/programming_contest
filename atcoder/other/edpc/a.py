n = int(input())
H = list(map(int,input().split()))
inf = 10**10
dp = [inf]*n
dp[0] = 0
for i in range(1,n):
    for j in range(max(0,i-2),i):
        dp[i] = min(dp[i],dp[j]+abs(H[i]-H[j]))
print(dp[-1])