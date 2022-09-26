n,l,r = map(int,input().split())
A = list(map(int,input().split()))
inf = 10**20

def calc(A,l):
    dp = [[inf]*2 for i in range(n+1)]
    dp[0] = [0,0]
    for i,a in enumerate(A):
        dp[i+1][0] = dp[i][0]+l
        dp[i+1][1] = min(dp[i])+a

    return dp

dpl = calc(A,l)
dpr = calc(A[::-1],r)
dpr = dpr[::-1]
ans = inf

for i in range(n+1):
    ans = min(ans,min(dpl[i])+min(dpr[i]))
print(ans)