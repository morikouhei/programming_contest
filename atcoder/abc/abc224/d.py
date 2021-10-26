from collections import deque
m = int(input())
e = [[] for i in range(9)]
for i in range(m):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

P = list(map(int,input().split()))
now = [8]*9
for i,p in enumerate(P):
    now[p-1] = i
num = ""
for p in now:
    num += str(p)
dis = {num:0}
q = deque([])
q.append(num)
while q:
    num = q.popleft()
    d = dis[num]
    for i in range(9):
        if num[i] != "8":
            continue
        for nex in e[i]:
            nnum = ""
            for j in range(9):
                if j == nex:
                    nnum += "8"
                elif j == i:
                    nnum += num[nex]
                else:
                    nnum += num[j]
            if nnum in dis:
                if dis[nnum] > d+1:
                    dis[nnum] = d+1
                    q.append(nnum)
            else:
                dis[nnum] = d+1
                q.append(nnum)

ans = ""
for i in range(9):
    ans += str(i)

if ans in dis:
    print(dis[ans])
else:
    print(-1)

