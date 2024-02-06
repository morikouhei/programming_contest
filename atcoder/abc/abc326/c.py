n,m = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = 0
now = 0
for i in range(n):
    a = A[i]
    while now < n and A[now] -  a < m:
        now += 1
    ans = max(ans,now-i)
print(ans)