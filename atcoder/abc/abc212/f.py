from heapq import heappop, heappush
n,m,q = map(int,input().split())
p = [[] for i in range(n)]
ans = [[0] for i in range(q)]
bas = []
inf = 10**10
for i in range(m):
    a,b,s,t = map(int,input().split())
    bas.append([s,t,a-1,b-1,i])
query = []
for i in range(q):
    x,y,z = map(int,input().split())
    query.append([x,-1,y-1,z,i])

event = []
for b in bas:
    event.append(b)
for i in query:
    event.append(i)
event.sort()

for e in event:
    print(e)
    print(p)
    if e[1] == -1:
        x,_,y,z,i = e
        heappush(p[y],[x,z,i])
    else:
        s,t,a,b,i = e
        while True:
            if p[a] == [] or  p[a][0][0] > s:
                break
            x,z,ind = heappop(p[a])
            if z <= s:
                ans[ind] = [a+1]
            elif z <= t:
                ans[ind] = [a+1,b+1]
            else:
                heappush(p[b],[t,z,ind])
print(p)
for i in range(n):
    for x,z,ind in p[i]:
        ans[ind] = [i+1]

for i in ans:
    print(*i)