n,m = map(int,input().split())
e = [[] for i in range(n)]
count = [0]*n
for i in range(m):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    e[x].append(y)
    count[y] += 1


q = []
ans = [0]*n
for i in range(n):
    if count[i] == 0:
        q.append(i)


used = 1
while q:
    if len(q) > 1:
        print("No")
        exit()
    now = q.pop()
    ans[now] = used
    used += 1
    for nex in e[now]:
        count[nex] -= 1
        if count[nex] == 0:
            q.append(nex)

if used == n+1:
    print("Yes")
    print(*ans)
else:
    print("No")