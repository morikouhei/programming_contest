S = input()
mod = 998244353
ans = 0
cum = 0
n = len(S)
pow2 = [1]
for i in range(n+5):
    pow2.append(pow2[-1]*2%mod)
for i,s in enumerate(S):
    s = int(s)
    ans += cum*pow2[n-1-i]%mod
    ans %= mod
    cum *= 10
    cum += pow2[i]*s
    cum %= mod
print((ans+cum)%mod)