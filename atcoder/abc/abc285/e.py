n = int(input())
A = [0]+list(map(int,input().split()))

work = [0]*(n+1)
for i in range(1,n):
    
    count = 0
    for j in range(1,i+1):
        count += A[min(j,i+1-j)]
    work[i] = count
dp = [0]*(n+1)
dp[0] = 0
for i in range(1,n+1):
    for j in range(i):
        dp[i] = max(dp[i],dp[j]+work[i-j-1])
print(dp[-1])