from collections import Counter

def solve():
    n = int(input())
    A = list(map(int,input().split()))
    M = 2*10**5+5
    C = Counter(A)
    dp = [0]*M
    for i in range(1,M):
        if i in C:
            dp[i] += C[i]
        now = i*2
        while now < M:
            dp[now] = max(dp[now],dp[i])
            now += i
    return n-max(dp)  


t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)