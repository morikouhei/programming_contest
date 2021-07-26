n = int(input())
C = list(map(int,input().split()))
C.sort()
mod = 10**9+7
ans = C[0]
for i in range(1,n):
    ans *= C[i]-i
    ans %= mod
print(ans)
