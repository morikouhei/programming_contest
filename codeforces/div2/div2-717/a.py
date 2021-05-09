t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    now = 0
    while now < n-1 and k:
        if A[now] <= k:
            A[-1] += A[now]
            k -= A[now]
            A[now] = 0
        else:
            A[now] -= k
            A[-1] += k
            k = 0
        now += 1
    print(*A)
            