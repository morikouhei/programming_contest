n,k = map(int,input().split())
ab = []
a = []
b = []
for i in range(n):
    t,c,d = map(int,input().split())
    if c and d == 0:
        a.append(t)
    elif d and c == 0:
        b.append(t)
    elif c*d:
        ab.append(t)
a.sort()
b.sort()
ab.sort()
la = len(a)
lb = len(b)
lab = len(ab)
if la+lab < k or lb+lab < k:
    print(-1)
    exit()
if lb > la:
    la,lb = lb,la
    a,b = b,a

ans = 0
if lab >= k:
    ans += sum(ab[:k])
    now = k-1
    na = 0
    nb = 0
    while nb < lb and now >= 0 and ab[now] > a[na]+b[nb]:
        ans -= ab[now]-a[na]-b[nb]
        na += 1
        nb += 1
        now -= 1
else:
    ans += sum(ab) +sum(b[:k-lab])+sum(a[:k-lab])
    now = lab-1
    na = k-lab
    nb = k-lab
    while nb < lb and now >= 0 and ab[now] > a[na]+b[nb]:
        ans -= ab[now]-a[na]-b[nb]
        na += 1
        nb += 1
        now -= 1  

print(ans)


