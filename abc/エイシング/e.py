import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    l = [[] for i in range(n+1)]
    r = [[] for i in range(n+1)]
    ans = 0
    for i in range(n):
        a,b,c = map(int,input().split())
        if b > c:
            l[a].append(b-c)
            ans += c
        else:
            r[a].append(c-b)
            ans += b
    q = []
    for i, lx in enumerate(l):
        for x in lx:
            if len(q) < i:
                heapq.heappush(q,x)
            else:
                heapq.heappushpop(q,x)
    ans += sum(q)
    q = []
    for i,rx in enumerate(r[::-1][1:],1):
        for x in rx:
            if len(q) < i:
                heapq.heappush(q,x)
            else:
                heapq.heappushpop(q,x)
    ans += sum(q)
    print(ans)