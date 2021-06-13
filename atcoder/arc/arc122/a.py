n = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

dp = [A[0],0]
pat = [1,0]
for a in A[1:]:
    ndp = [0,0]
    npat = [0,0]
    ndp[0] += sum(dp)+a*sum(pat)
    ndp[0] %= mod
    ndp[1] = dp[0]-pat[0]*a
    npat[0] = sum(pat)%mod
    npat[1] = pat[0]
    ndp[1] %= mod
    dp = ndp
    pat = npat

print(sum(dp)%mod)