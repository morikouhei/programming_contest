n,m = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
ans = [0]*m
ids = [[] for i in range(m+5)]
for i,(a,b) in enumerate(AB):
    ids[a].append(i)
    ids[b].append(i)

imos = [0]*(m+5)
num = [0]*(m+5)
ok = [0]*(m+5)

count = 0

used = [0]*n
now = 0

for id in range(1,m+1):
    if now < id:
        now = id
        for d in ids[id]:
            used[d] += 1
            if used[d] == 1:
                count += 1
    while now <= m and count < n:
        now += 1
        for d in ids[now]:
            used[d] += 1
            if used[d] == 1:
                count += 1
    
    if count == n:
        dif = now-id
       
        imos[dif+1] += 1
        imos[m+2-id] -= 1
    
    for d in ids[id]:
        used[d] -= 1
        if used[d] == 0:
            count -= 1
            
for i in range(1,m+1):
    ans[i-1] = imos[i]
    imos[i+1] += imos[i]


print(*ans)