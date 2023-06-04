from collections import deque
n,m = map(int,input().split())


e = [[] for i in range(n+m)]
for i in range(n):
    a = int(input())

    s = list(map(int,input().split()))
    if 1 in s and m in s:
        print(0)
        exit()
    
    for id in s:
        nid = n+id-1
        e[i].append(nid)
        e[nid].append(i)


inf = 10**10
dis = [inf]*(n+m)
dis[n] = 0

q = deque([n])
while q:
    now = q.popleft()
    for nex in e[now]:
        if dis[nex] > dis[now]+1:
            dis[nex] = dis[now]+1
            q.append(nex)

ans =  dis[-1]
# print(dis)
if ans == inf:
    ans = -1
else:
    ans //= 2
    ans -= 1
print(ans)
