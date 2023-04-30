import sys
sys.setrecursionlimit(3*10**5)
n = int(input())
div = [2,3,5]
nums = []

mod = 998244353
for d in div:
    num = 0
    while n%d == 0:
        n //= d
        num += 1
    nums.append(num)

if n != 1:
    print(0)
    exit()
# print(nums)

ans = 0
dp = [[[[0]*(nums[2]+1) for i in range(nums[1]+1)] for j in range(nums[0]+1)] for k in range(sum(nums)+1)]
dp[0][-1][-1][-1] = 1
for i in range(sum(nums)+1):
    for j in range(nums[0]+1)[::-1]: ## 2
        for k in range(nums[1]+1)[::-1]: ## 3
            for m in range(nums[2]+1)[::-1]: ## 5
                num = dp[i][j][k][m]

                if num == 0:
                    continue
                # print(i,j,k,m,num)
                if j:
                    dp[i+1][j-1][k][m] += num
                    dp[i+1][j-1][k][m] %= mod
                
                if m:
                    dp[i+1][j][k][m-1] += num
                    dp[i+1][j][k][m-1] %= mod

                if j > 1:
                    dp[i+1][j-2][k][m] += num
                    dp[i+1][j-2][k][m] %= mod

                if j and k:
                    dp[i+1][j-1][k-1][m] += num
                    dp[i+1][j-1][k-1][m] %= mod
                
                if k:
                    dp[i+1][j][k-1][m] += num
                    dp[i+1][j][k-1][m] %= mod



for i in range(sum(nums)+1):
    if dp[i][0][0][0]:
        ans += dp[i][0][0][0] * pow(pow(5,i,mod),mod-2,mod)
        ans %= mod
print(ans)