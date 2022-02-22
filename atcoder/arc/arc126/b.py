import bisect

inf = 10**10

n,m = map(int,input().split())
e = [[] for i in range(n)]
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)


lis = [inf]*(n+1)
for i,ne in enumerate(e):
    ne.sort(reverse=True)
    for ind in ne:
        bind = bisect.bisect_left(lis,ind)
        lis[bind] = ind

print(bisect.bisect_left(lis,inf))
