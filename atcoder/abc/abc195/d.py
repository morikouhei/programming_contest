from heapq import heappop, heappush
n,m,q = map(int,input().split())
wv = [tuple(map(int,input().split())) for i in range(n)]
wv.sort()
X = list(map(int,input().split()))

for _ in range(q):
    l,r = map(int,input().split())

    cand = []
    for i in range(m):
        if l <= i+1 <= r:
            continue
        cand.append(X[i])
    cand.sort()
    h = []
    now = 0
    count = 0
    for i in cand:
        while now < n and wv[now][0] <= i:
            heappush(h,-wv[now][1])
            now += 1
        if h:
            count -= heappop(h)
    print(count)