def solve():
    n = int(input())
    A = list(map(int,input().split()))
    dp = [0]*(201)
    dp[0] = 1
    for a in A:
        for i in range(200)[::-1]:
            if dp[i]:
                dp[i+a] = 1
    if sum(A) % 2 == 0 and dp[sum(A)//2]:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)