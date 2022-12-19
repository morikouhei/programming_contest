from itertools import count


n,k,c = map(int,input().split())
mod = 998244353

dp = [0]*n
base = c*(c-1)%mod

def get(r,l):
    return (dp[r]-dp[l])%mod
for i in range(1,n):
    count = base
    count += get(i-1,max(0,i-k+1))
    count += get(max(0,i-k+1),0)*(c-1)
    count %= mod
    dp[i] = (count + dp[i-1]) % mod
ans = dp[-1]+c    
print(ans%mod)