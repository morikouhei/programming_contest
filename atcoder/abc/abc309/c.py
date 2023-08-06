n,k = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]

s = set()
for a,b in AB:
    s.add(a)
s.add(0)
le = len(s)
s = sorted(s)

dic = {x:i for i,x in enumerate(s)}

imos = [0]*le

for a,b in AB:
    imos[0] += b
    imos[dic[a]] -= b

ans = 0
for i in range(le-1):
    imos[i+1] += imos[i]

    l = s[i]
    r = s[i+1]
    if imos[i] <= k:
        print(l+1)
        exit()

print(r+1)