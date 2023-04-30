from heapq import heappop,heappush

n,k = map(int,input().split())
A = list(map(int,input().split()))


h = []
for a in A:
    heappush(h,a)

last = 0
while k:
    now = heappop(h)
    if last == now:
        continue
    k -= 1
    last = now
    for a in A:
        heappush(h,now+a)

print(last)