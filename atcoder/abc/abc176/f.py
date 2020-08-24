n = int(input())
A = list(map(int,input().split()))

dp = [[-float("INF")]*(n+1) for i in range(n+1)]
low = [-float("INF")]*(n+1)
m = 0
a,b = A[:2]
dp[a][b] = 0
dp[b][a] = 0
low[a] = 0
low[b] = 0
base = 0

for _ in range(1,n):
    a,b,c = A[3*_-1:3*_+2]
    q = []
    if a==b==c:
        base += 1
        continue
    m1 = m
    for j in range(3):
        q.append((a,b,max(m,dp[c][c]+1)))
        m1 = max(m1,dp[c][c]+1)

        for i in range(1,n+1):
            q.append((a,i,low[i]))
        if a==b:
            for i in range(1,n+1):
                q.append((c,i,dp[a][i]+1))
                m1 = max(m1,dp[a][i]+1)
        a,b,c = b,c,a

    for a,b,v in q:
        dp[a][b] = max(dp[a][b],v)
        dp[b][a] = max(dp[b][a],v)
        low[a] = max(low[a],v)  
        low[b] = max(low[b],v)      
    m = m1
    
print(max(m,dp[A[-1]][A[-1]]+1)+base)


