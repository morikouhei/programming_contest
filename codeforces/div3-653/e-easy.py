n,m,k = map(int,input().split())
ab = []
a = []
b = []
other = []
l = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    t,c,d = l[i]
    if c and d == 0:
        a.append([t,i+1])
    elif d and c == 0:
        b.append([t,i+1])
    elif c*d:
        ab.append([t,i+1])
    else:
        other.append([t,i+1])
a.sort()
b.sort()
ab.sort()
la = len(a)
lb = len(b)
lab = len(ab)
s = set()
dis = set()
if la+lab < k or lb+lab < k:
    print(-1)
    exit()
if lb > la:
    la,lb = lb,la
    a,b = b,a

if lab >= k:
    for i in range(k):
        
        s.add(ab[i][1])
    now = k-1
    na = 0
    nb = 0
    
else:
    for i,j in ab:
        
        s.add(j)
    for i in range(k-lab):
        s.add(a[i][1])
        s.add(b[i][1])
    now = lab-1
    na = k-lab
    nb = k-lab
while nb < lb and now >= 0 and ab[now][0] >= a[na][0]+b[nb][0]:
    s.add(a[na][1])
    s.add(b[nb][1])
    dis.add(ab[now][1])
    na += 1
    nb += 1
    now -= 1
s2 = set()
for i in s:
    if i in dis:
        continue
    s2.add(i)
s = set()
dis = set()
if len(s2) >= m:
    q = len(s2)-m

    for i in range(q):
        na -= 1
        nb -= 1
        now += 1
        if now == lab:
            print(-1)
            exit()
        s.add(ab[now][1])
        dis.add(a[na][1])
        dis.add(b[nb][1])
else:
    for i in range(la):
        if a[i][1] not in s2:
            other += a[i:]
            break
    for i in range(lb):
        if b[i][1] not in s2:
            other += b[i:]
            break
    for i in range(lab):
        if ab[i][1] not in s2:
            other += ab[i:]
            break
    other.sort()
    for i in range(m-len(s2)):
        s.add(other[i][1])

s |= s2
ans = 0
count = []
for i in s:
    if i in dis:
        continue
    count.append(i)
    ans += l[i-1][0]
print(ans)
print(*count)



