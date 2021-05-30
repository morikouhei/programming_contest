n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
mod = 10**9+7
ans = 1
for a in A:
    ans *= sum(a)
    ans %= mod
print(ans)