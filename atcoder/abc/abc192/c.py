n,k = map(int,input().split())

a = n
for i in range(k):
    s = list(str(a))
    s.sort()
    g2 = 0
    for i in range(len(s)):
        g2 *= 10
        g2 += int(s[i])
    s.sort(reverse=True)
    g1 = 0
    for i in range(len(s)):
        g1 *= 10
        g1 += int(s[i])
    a = g1-g2
print(a)
