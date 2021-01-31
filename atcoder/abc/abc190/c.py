n,m = map(int,input().split())
ab = [tuple(map(int,input().split())) for i in range(m)]
k = int(input())
cd = [tuple(map(int,input().split())) for i in range(k)]
ans = 0
for i in range(1<<k):
    count = [0]*(n+1)
    for j in range(k):
        if i >> j & 1:
            count[cd[j][0]] += 1
        else:
            count[cd[j][1]] += 1
    c = 0
    for a,b in ab:
        if count[a] and count[b]:
            c += 1
    ans = max(ans,c)
print(ans)