n,x,y = map(int,input().split())
A = list(map(int,input().split()))
M = 10**4+5

def calc(s,t,lis):
    dp = [0]*(2*M)
    dp[s] = 1
    for a in lis:
        ndp = [0]*(2*M)
        for i in range(-M,M):
            if dp[i] == 0:
                continue
            if i+a < M:
                ndp[i+a] = 1
            if i-a > -M:
                ndp[i-a] = 1
        dp = ndp
    return dp[t]

if calc(0,y,A[1::2]) == 0 or calc(A[0],x,A[2::2]) == 0:
    print("No")
else:
    print("Yes")

