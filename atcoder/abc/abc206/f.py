import sys
sys.setrecursionlimit(2*10**6)
def solve():
    n = int(input())

    dp = [[-1]*101 for i in range(101)]
    LR = [list(map(int,input().split())) for i in range(n)]
    def dfs(l,r):
        if dp[l][r] != -1:
            return dp[l][r]
        s = set()
        for x,y in LR:
            if l <= x and y <= r:
                s.add(dfs(l,x)^dfs(y,r))

        dp[l][r] = 0
        for i in range(100):
            if i not in s:
                dp[l][r] = i
                return i
    ans = dfs(1,100)
    if ans:
        print("Alice")
    else:
        print("Bob")
t = int(input())
for _ in range(t):
    solve()