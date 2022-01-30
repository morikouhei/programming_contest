n = int(input())
A = list(map(int,input().split()))
mod = 998244353

dp = [0]*(n+1)
dp[0] = 1

ma = []
mi = []
ma_v = []
mi_v = []
max_sum = 0
min_sum = 0

for i in range(n):
    a = A[i]
    count = dp[i]
    while ma and ma[-1] < a:
        last_v = ma_v.pop()
        last_ma = ma.pop()
        max_sum -= last_ma*last_v
        count += last_v
        max_sum %= mod
        count %= mod

    max_sum += count*a
    max_sum %= mod
    ma.append(a)
    ma_v.append(count)


    count = dp[i]
    while mi and mi[-1] > a:
        last_v = mi_v.pop()
        last_mi = mi.pop()
        min_sum -= last_mi*last_v
        count += last_v
        min_sum %= mod
        count %= mod

    min_sum += count*a
    min_sum %= mod
    mi.append(a)
    mi_v.append(count)

    dp[i+1] = max_sum-min_sum
    dp[i+1] %= mod

print(dp[-1])