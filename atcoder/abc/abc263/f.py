n = int(input())
n2 = 1<<n
C = [list(map(int,input().split())) for i in range(n2)]

dpmax = [0]*(n2*2)
dp = [0]*n2

for i in range(1,n+1):
    for j in range(n2):
        id  = j+n2
        tid = id >> i
        t2id = id >> (i-1)
        target = tid*2 if tid*2 != t2id else tid*2+1
        dp[j] = dp[j]+dpmax[target]
        dpmax[tid] = max(dpmax[tid],dp[j]+C[j][i-1])

print(dpmax[1])