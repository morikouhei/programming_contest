n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [0,1]
dic = {}
now = 0
for i,a in enumerate(A[:-1],1):
    now += a

    count = dp[-1]-dp[dic.get(now,0)]
    count %= mod
    dp.append((dp[-1]+count)%mod)
    dic[now] = i
print(dp[-1])
print(dp)