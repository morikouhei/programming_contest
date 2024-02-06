n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

e = [[] for i in range(n)]
for a,b in zip(A,B):
    a,b = a-1,b-1
    e[a].append(b)
    e[b].append(a)


vis = [-1]*n

for i in range(n):
    if vis[i] != -1:
        continue

    q = [i]
    vis[i] = 0
    while q:
        now = q.pop()
        for nex in e[now]:
            if vis[nex] == -1:
                vis[nex] = vis[now]^1
                q.append(nex)

            else:
                if vis[nex] == vis[now]:
                    print("No")
                    exit()
print("Yes")