n,m = map(int,input().split())
A = list(map(int,input().split()))

ans = -10**20

s = 0
count = 0
for i in range(m):
    count += A[i]
    s += A[i]*(i+1)

ans = max(ans,s)
for i in range(m,n):
    s -= count
    count -= A[i-m]
    count += A[i]
    s += A[i]*m
    ans = max(ans,s)
print(ans)
