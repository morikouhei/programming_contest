import heapq

n = int(input())
h = []
l = [list(map(int,input().split())) for i in range(n)]
l.sort()

count = 0
now = 0
for i in range(n):
    while now < n and l[now][0] <= i+1:
        heapq.heappush(h,-l[now][1])
        now += 1
    count -= heapq.heappop(h)
    print(count)
