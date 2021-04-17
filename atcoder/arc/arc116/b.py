n = int(input())
A = list(map(int,input().split()))
A.sort()
mod = 998244353

ans = 0
cum = 0

for i,a in enumerate(A):
    ans += (cum+a)*a
    ans %= mod
    cum *= 2
    cum += a
    cum %= mod
print(ans)
