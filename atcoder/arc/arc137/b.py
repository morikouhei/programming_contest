n = int(input())
A = list(map(int,input().split()))

mi = 0
ma = 0
now = 0

c1 = 0
c2 = 0
for a in A:
    if a:
        now -= 1
    else:
        now += 1
    c1 = max(c1,now-mi)
    c2 = max(c2,ma-now)
    ma = max(ma,now)
    mi = min(mi,now)
print(c1+c2+1)