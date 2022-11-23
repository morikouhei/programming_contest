n = int(input())
mod = 998244353


base = pow(2,pow(2,n,mod),mod)
base = pow(2,pow(2,n,mod-1),mod)
# print(base)
c = pow(2,n,mod-1)
# print(c,pow(2,n,mod-1))
cal = pow(2,c,mod)
inv = pow(2,n+1,mod)
inv = pow(inv,mod-2,mod)
cal = cal*inv%mod
# print(cal)
print((base-cal+1)%mod)
c = (pow(2,n,mod)-n-1)%mod
c = pow(2,c,mod)
# print(c)
base -= c-1
# print(base%mod)
def solve(x):

    two = 1<<x
    dp = [[0]*two for i in range(2)]
    dp[0][0] = 1

    for i in range(two):
        ndp = [[0]*two for i in range(2)]
        for j in range(two):
            for k in range(2):
                if dp[k][j] == 0:
                    continue
                ndp[k][j] += dp[k][j]
                ndp[k^1][j^i] += dp[k][j]
        dp = ndp
        # print(dp)

    return dp[0][0]

def solve2(x):
    
    ans = 0
    # print(x,pow(2,x))
    for i in range(pow(2,pow(2,x))):
        if bin(i).count("1")%2:
            continue
        xor = 0
        for j in range(pow(2,x)):
            if i >> j & 1:
                xor ^= j
        if xor == 0:
            ans += 1
    return ans
# for i in range(1,5):
#     print(solve(i))
#     print(solve2(i))

# for i in range(1,8):
#     x = pow(2,i-1)-i
#     x = pow(2,x)
#     print(x)