from heapq import heappush,heappop

n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    u,v,w = map(int,input().split())
    u,v = u-1,v-1
    e[u].append([v,w])
    e[v].append([u,w])

k = int(input())
A = list(map(int,input().split()))
D = int(input())
X = list(map(int,input().split()))

day = [n+1]*n

h_all = []

for a in A:
    a -= 1
    day[a] = 0

for i in range(n):
    if day[i]:
        continue
    for nex,w in e[i]:
        if day[nex] == 0:
            continue
        heappush(h_all,[w,nex])

# print(h_all)
status = [-1]*n
for d,x in enumerate(X,1):

    h_day = []
    while h_all:
        w,ind = h_all[0]
        # print(d,x,h_all[0])
        if day[ind] < d:
            heappop(h_all)
        elif x >= w:
            heappop(h_all)

            if day[ind] == d:
                continue

            day[ind] = d
            status[ind] = x-w
            heappush(h_day,[-(x-w),ind])

        else:
            break

    # print(h_day)
    while h_day:
        nd,ind = heappop(h_day)
        nd *= -1
        if status[ind] != nd:
            continue

        for nex,w in e[ind]:
            if day[nex] < d:
                continue

            if day[nex] > d:
                if w <= nd:
                    day[nex] = d
                    status[nex] = nd-w
                    heappush(h_day,[-(nd-w),nex])
                else:
                    heappush(h_all,[w,nex])
            else:
                if nd-w >= 0 and nd-w > status[nex]:
                    status[nex] = nd-w
                    heappush(h_day,[-(nd-w),nex])


for i in day:
    if i == n+1:
        i = -1
    print(i)