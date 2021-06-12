def solve():
    n,k = map(int,input().split())
    ans = ["a"]*n
    now = n-2
    while k:
        if k > n-1-now:
            k -= n-1-now
            now -= 1
        else:
            ans[now] = "b"
            ans[n-k] = "b"
            print(*ans,sep="")
            return

t = int(input())
for _ in range(t):
    solve()