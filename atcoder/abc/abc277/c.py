n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
s = set()
s.add(1)
for a,b in AB:
    s.add(a)
    s.add(b)
s = sorted(s)
le = len(s)
dic = {x:i for i,x in enumerate(s)}
e = [[] for i in range(le)]
for a,b in AB:
    e[dic[a]].append(dic[b])
    e[dic[b]].append(dic[a])

vis = [0]*le
ans = 1
q = [0]
vis[0] = 1
while q:
    now = q.pop()
    ans = max(ans,s[now])
    for nex in e[now]:
        if vis[nex]:
            continue
        vis[nex] = 1
        q.append(nex)
print(ans)
