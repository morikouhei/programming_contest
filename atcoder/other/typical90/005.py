n,b,k = map(int,input().split())
C = list(map(int,input().split()))
mod = 10**9+7

def calc(lis1,lis2,ten):
    ans = [0]*b
    for i in range(b):
        for j in range(b):
            now = (i*ten+j)%b
            ans[now] += lis1[i]*lis2[j]
            ans[now] %= mod
    return ans

dp = [0]*b
for c in C:
    dp[c%b] += 1
ans = [0]*b
ans[0] = 1
ten = 10
while n:
    if n%2:
        ans = calc(ans,dp,ten)
    dp = calc(dp,dp,ten)
    ten = ten**2%b
    n //= 2

print(ans[0])

