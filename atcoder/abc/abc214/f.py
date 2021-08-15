S = input()
n = len(S)
mod = 10**9+7
next = [[n]*26 for i in range(n+1)]
for i in range(n)[::-1]:
    for j in range(26):
        next[i][j] = next[i+1][j]
    next[i][ord(S[i])-ord("a")] = i

dp = [0]*(n+1)
for i in range(26):
    if next[0][i] >= n:
        continue
    dp[next[0][i]+1] += 1
for i in range(1,n):
    for j in range(26):
        nex = next[i][j]
        if nex == i:
            nex = next[nex+1][j]
        if nex >= n:
            continue
        dp[nex+1] += dp[i]
        dp[nex+1] %= mod
print(sum(dp)%mod)