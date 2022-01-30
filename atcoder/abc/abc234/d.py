from heapq import heappush, heappop
n,k = map(int,input().split())
P = list(map(int,input().split()))

h = []
for i,p in enumerate(P):
    heappush(h,p)
    if i >= k:
        heappop(h)
    if i >= k-1:
        print(h[0])
    