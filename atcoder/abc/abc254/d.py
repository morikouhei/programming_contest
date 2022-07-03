from sqlite3 import connect


n = int(input())
divs = [0]*(n+1)
for i in range(2,n+1):
    if divs[i]:
        continue
    for j in range(i,n+1,i):
        if divs[j]:
            continue
        divs[j] = i


ans = 0
for i in range(1,n+1):

    pair = 1
    now = i
    while now > 1:
        d = divs[now]
        if pair%d == 0:
            pair //= d
        else:
            pair *= d
        now //= d
    
    if pair > n:
        continue

    l = 1
    r = n+1
    while r > l + 1:
        m = (r+l)//2
        if m**2*pair > n:
            r = m
        else:
            l = m
    ans += l
    # print(i,pair,l)
print(ans)