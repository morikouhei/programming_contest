N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 0

count = 0
r = 0
for i in range(N):
    while r < N and count < K:
        count += A[r]
        r += 1
    if count >= K:
        ans += N + 1 - r
    count -= A[i]
print(ans)
