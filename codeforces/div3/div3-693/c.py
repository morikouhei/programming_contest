def solve():
    n = int(input())
    A = list(map(int,input().split()))
    dp = [0]*n
    for i in range(n)[::-1]:
        a = A[i]
        if a+i < n:
            dp[i] = a+dp[a+i]
        else:
            dp[i] = a
    return max(dp)

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)