n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

inf = 10**20

## 0 = 0, 1 = x (0 or 1)
def calc(x):

    dp = [inf]*2
    dp[x] = A[0]*(1^x)
    for i in range(1,n):
        dp = [min(dp[1],dp[0]+B[i-1])+A[i],min(dp[0],dp[1]+B[i-1])]
    dp[x] += B[-1]
    return dp


ans = min(min(calc(0)),min(calc(1)))
print(ans)