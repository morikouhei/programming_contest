n = int(input())
l = list(map(int,input().split()))

ans = 0
s = set()
for i in l:
    if i > 0:
        s.add(i)
for i in s:
    
    now = 0
    for j in l:
        if j > i:
            now -= float("INF")
        else:
            now += j
        if now <= 0:
            now = 0
        else:
            ans = max(ans,now-i)
print(ans)