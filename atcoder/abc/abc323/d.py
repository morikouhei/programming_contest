from heapq import heappop,heappush
n = int(input())
SC = [list(map(int,input().split())) for i in range(n)]

dic = {s:c for s,c in SC}

h = []
for s,c in SC:
    heappush(h,s)

ma = 0
for s,c in SC:
    ma = max(ma,s)
ans = 0

while h:
    s = heappop(h)
    c = dic[s]
    if s > ma:
    
        while c:
            ans += c%2
            c //= 2
        
        continue

    ans += c%2

    s *= 2
    c //= 2

    if s in dic:
        dic[s] += c
    else:
        dic[s] = c
        heappush(h,s)
print(ans)
    