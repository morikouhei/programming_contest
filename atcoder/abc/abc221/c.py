n = input()
l = len(n)

ans = 0

for i in range(1<<l):
    a = []
    b = []
    for j in range(l):
        if i >> j & 1:
            a.append(n[j])
        else:
            b.append(n[j])
    if a == [] or b == []:
        continue
    na = 0
    a.sort(reverse=True)
    b.sort(reverse=True)
    na = ""
    for i in a:
        na += i
    na = int(na)
    nb = ""
    for i in b:
        nb += i
    nb = int(nb)
    ans = max(ans,na*nb)
print(ans)