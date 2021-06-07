n = int(input())
T = list(map(int,input().split()))
M = 10**5
dp = [0]*(M+5)
dp[0] = 1
for t in T:
    for i in range(M)[::-1]:
        if dp[i]:
            dp[i+t] = 1

s = sum(T)
ans = s
for i in range(M+1):
    if dp[i]:
        ans = min(ans,max(i,s-i))

print(ans)