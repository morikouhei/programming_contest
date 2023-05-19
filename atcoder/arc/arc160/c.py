n = int(input())
A = list(map(int,input().split()))
mod = 998244353

M = 2*10**5 + 100

nums = [0]*M
for a in A:
    nums[a] += 1


dp = [1]

for num in nums:
    nsize = (num + len(dp)-1) // 2

    ndp = [0]*(nsize+1)

    for i,d in enumerate(dp):
        ndp[(i+num)//2] += d
        ndp[(i+num)//2] %= mod

    dp = ndp
    for i in range(1,len(dp))[::-1]:
        dp[i-1] += dp[i]
        dp[i-1] %= mod

print(dp[0])
