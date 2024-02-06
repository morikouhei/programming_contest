from heapq import heappush,heappop
n = int(input())
TD = [list(map(int,input().split())) for i in range(n)]
TD.sort()

ans = 0
h = []
t = 0

event = {}
for t,d in TD:
    if t not in event:
        event[t] = []
    event[t].append(t+d)

events = sorted(event.keys())
events.append(10**20)
for i in range(len(events)-1):
    t = events[i]

    nt = events[i+1]

    for v in event[t]:
        heappush(h,v)

    while h and t < nt:
        v = heappop(h)
        if v >= t:
            ans += 1
            t += 1
print(ans)