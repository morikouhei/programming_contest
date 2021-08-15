S = input()
n = len(S)
mod = 10**9+7
next = [[n]*26 for i in range(n+1)]
for i in range(n)[::-1]:
    for j in range(26):
        next[i][j] = next[i+1][j]
    next[i][ord(S[i])-ord("a")] = i

print(next)
dp = [0]*(n+1)
dp[0] = 1
for i in range(n):
    print(S[i])
    for j in range(26):
        if next[i][j] >= n:
            continue
        
        dp[next[i][j]+1] += dp[i]
        dp[next[i][j]+1] %= mod
    print(dp)
ans = (sum(dp)-1)%mod
print(ans)