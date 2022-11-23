n = int(input())
S = []
for i in range(n):
    s = input()
    num = 0
    for j in range(n):
        if s[j] == ".":
            num += 1<<j
    S.append(num)

mod = 998244353
mask = (1<<n)-1
ans = 0

dp = [[0]*(1<<n) for i in range(n+1)]

score = [0]*(1<<n)
for i in range(1<<n):
    score[i] = bin(i).count("1")
dp[0][0] = 1

for i in range(n):
    
    check = [1]*(1<<n)
    for j in range(1<<n):
        if S[i] & j == j:
            check[j] = 1
        else:
            check[j] = 0
    # print(check)
    for na in range(n+1)[::-1]:
        for b in range(1<<n)[::-1]:
            if dp[na][b] == 0:
                continue
            x = dp[na][b]
            r = mask^b
            v = (-1) & r
            # print(b,r,v)
            while v:
                if check[v]:
                    nna = max(na,score[v])
                    # print(v,nna)
                    if nna > na:
                        # print(nna,v|b,x)
                        dp[nna][v|b] += x
                        dp[nna][v|b] %= mod
                    else:
                        dp[na][v|b] += x
                        dp[na][v|b] %= mod


                v = (v-1) & r

for i in range(n+1):
    # print(dp[i])
    ans += sum(dp[i])%mod*i
    ans %= mod
print(ans)