p = int(input())
mod = 998244353
div = set()
p -= 1
for i in range(1,int(p**0.5)+1):S
    if p%i:
        continue
    div.add(i)
    div.add(p//i)
div = sorted(list(div))

dp = [0]*len(div)
for i in range(len(div))[::-1]:
    dp[i] = p//div[i]
    for j in range(i+1,len(div)):
        if div[j]%div[i]:
            continue
        dp[i] -= dp[j]
        dp[i] %= mod
ans = 1
for i in range(len(div)):
    ans += dp[i]*p//div[i]
    ans %= mod
print(ans)