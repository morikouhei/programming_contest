n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
s = set()
for a,b in AB:
    s.add(a)
    s.add(a+b)

s = sorted(s)
dic = {x:i for i,x in enumerate(s)}
dic2 = {i:x for i,x in enumerate(s)}
l = len(s)
imos = [0]*(l+5)
for a,b in AB:
    imos[dic[a]] += 1
    imos[dic[a+b]] -= 1

for i in range(l-1):
    imos[i+1] += imos[i]

ans = [0]*(n+1)
for i in range(l-1):
    c = imos[i]
    ans[c] += dic2[i+1]-dic2[i]
print(*ans[1:])
