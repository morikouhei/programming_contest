from heapq import heappush,heappop
n,m = map(int,input().split())
P = list(map(int,input().split()))
L = list(map(int,input().split()))
D = list(map(int,input().split()))
LD = []
for l,d in zip(L,D):
    LD.append([l,d])


now = 0
ans = sum(P)
P.sort()
LD.sort()
h = []
for p in P:
    while now != m and LD[now][0] <= p:
        heappush(h,-LD[now][1])
        now += 1
    # print(p,now,h)
    while h:
        d = heappop(h)
        ans += d
        break

print(ans)