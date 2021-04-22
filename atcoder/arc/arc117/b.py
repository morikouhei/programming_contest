n = int(input())
A = sorted([0]+list(map(int,input().split())))
mod = 10**9+7
ans = 1
for a,na in zip(A,A[1:]):
    ans *= na-a+1
    ans %= mod
print(ans)