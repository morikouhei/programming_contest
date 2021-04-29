n,b = map(int,input().split())
s1 = set()
s2 = set()
N = str(n)
s1.add(1)
for num in N:
    num = int(num)
    ns1 = set()
    ns2 = set()
    ns2.add(1)
    for i in s1:
        for j in range(num+1):
            if j == num:
                ns1.add(i*j)
            else:
                ns2.add(i*j)
    for i in s2:
        for j in range(10):
            ns2.add(i*j)
    s1 = ns1
    s2 = ns2
s1 |= s2
if len(N) == 1:
    s1.remove(0)
ans = 0
for i in s1:
    cand = b+i
    s = str(cand)
    count = 1
    for j in s:
        count *= int(j)
    if count == i and cand <= n:
        ans += 1
print(ans)
