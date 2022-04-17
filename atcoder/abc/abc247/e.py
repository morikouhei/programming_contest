from collections import deque
n,x,y = map(int,input().split())
A = list(map(int,input().split()))

ans = 0
ys = deque()
xs = deque()
now = 0
for i,a in enumerate(A):
    now = max(now,i)
    while now < n and y <= A[now] <= x:
        if A[now] == y:
            ys.append(now)
        if A[now] == x:
            xs.append(now)
        now += 1

    while ys and ys[0] < i:
        ys.popleft()
    while xs and xs[0] < i:
        xs.popleft()

    if ys and xs:
        nind = max(xs[0],ys[0])
        ans += now-nind
print(ans)