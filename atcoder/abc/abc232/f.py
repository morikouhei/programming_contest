n,x,y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
inf = 10**20
dp = [inf]*(1<<n)
dp[0] = 0
for i in range(1<<n):
    
    count = bin(i).count("1")
    low = 0
    for j in range(n):
        if i >> j & 1:
            continue
        dp[i|1<<j] = min(dp[i|1<<j],dp[i]+low*y+x*abs(A[count]-B[j]))
        low += 1
print(dp[-1])