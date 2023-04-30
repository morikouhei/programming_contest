l,n1,n2 = map(int,input().split())
VL1 = [list(map(int,input().split())) for i in range(n1)]
VL2 = [list(map(int,input().split())) for i in range(n2)]


s = set()
now = 0
for v,l in VL1:
    now += l
    s.add(now)

now = 0
for v,l in VL2:
    now += l
    s.add(now)

s = sorted(s)
sl = len(s)
# print(s)
now = 0
le = 0
nVL1 = []
last = 0
for v,l in VL1:
    while now < sl and s[now] <= le+l:
        nVL1.append([v,s[now]-last])
        last = s[now]
        now += 1
    le += l

now = 0
le = 0
nVL2 = []
last = 0
for v,l in VL2:
    while now < sl and s[now] <= le+l:
        nVL2.append([v,s[now]-last])
        last = s[now]
        now += 1
    le += l


ans = 0
for (v1,l1),(v2,l2) in zip(nVL1,nVL2):
    if v1 == v2:
        ans += l1
print(ans)
