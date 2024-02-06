import bisect
D = int(input())

l = []
for i in range(2*10**6):
    l.append(i**2)


ans = D

for i in range(2*10**6):
    if i**2 > D:
        ans = min(ans,i**2-D)
        break
    x = bisect.bisect_left(l,D-i**2)
    ans = min(ans,abs(D-i**2-l[x]),abs(D-i**2-l[x-1]))
print(ans)