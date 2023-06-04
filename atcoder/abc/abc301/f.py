S = input()
mod = 998244353

dp = [0]*29
dp[0] = 1

used = set()
for s in S:
    ndp = [0]*29

    if "a" <= s <= "z":
        for i in range(27):
            ndp[i] += dp[i]
            ndp[i] %= mod

        ndp[28] += dp[27]+dp[28]
        ndp[28] %= mod


    elif "A" <= s <= "Z":
        ndp[1] += dp[0]
        if s in used:
            for i in range(1,28):
                ndp[27] += dp[i]
                ndp[27] %= mod

        else:
            size = len(used)
            inv = pow(26-size,mod-2,mod)
            for i in range(1,27):
                ndp[27] += dp[i]*(i-size)*inv%mod
       
                ndp[27] %= mod
                if i < 26:
                    ndp[i+1] += dp[i]*(26-i)*inv%mod
                    ndp[i+1] %= mod
            
            ndp[27] += dp[27]
            ndp[27] %= mod
            used.add(s)


    else:
        ndp[0] += dp[0]*26%mod
        ndp[1] += dp[0]*26%mod
        for i in range(1,27):
            ndp[i] += dp[i]*26
            ndp[i] %= mod
            ndp[i+1] += dp[i]*(26-i)
            ndp[i+1] %= mod

            ndp[27] += dp[i]*i
            ndp[27] %= mod
        ndp[27] += dp[27]*26
        ndp[27] %= mod
        ndp[28] += dp[27]*26 + dp[28]*26
        ndp[28] %= mod
    
    dp = ndp

print(sum(dp)%mod)