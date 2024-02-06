n,m = map(int,input().split())
A = list(map(int,input().split()))
now = 0
for i in range(1,n+1):
    while now < m and A[now] < i:
        now += 1
    print(A[now]-i)