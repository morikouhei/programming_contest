n,k = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9+7

dp = [0]*(k+1)
dp[0] = 1
sdp = [1]*(k+1)

for a in A:
    ndp = [0]*(k+1)
    nsdp = [0]*(k+1)
    for i in range(k+1):
        ndp[i] += sdp[i] 
        if i-a-1 >= 0:
            ndp[i] -= sdp[i-a-1]
        ndp[i] %= mod
        nsdp[i] += ndp[i]+nsdp[i-1]
        nsdp[i] %= mod
    dp = ndp
    sdp = nsdp

print(dp[-1])