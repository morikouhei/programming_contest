import heapq
q = int(input())
base = 0
dic = {}
h = []
for _ in range(q):
    l = list(map(int,input().split()))
    if l[0] == 3:
        print(heapq.heappop(h)+base)
    else:
        x = l[1]
        if l[0] == 1:
            heapq.heappush(h,x-base)
        else:
            base += x    