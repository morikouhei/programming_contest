from collections import deque
from heapq import heappop,heappush
q = int(input())

h = []
d = deque()
for _ in range(q):
    l = list(map(int,input().split()))
    if l[0] == 1:
        d.append(l[1])
    elif l[0] == 2:
        if h:
            print(heappop(h))
        else:
            print(d.popleft())
    else:
        while d:
            heappush(h,d.popleft())
