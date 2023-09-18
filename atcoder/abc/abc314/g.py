import sys
input = sys.stdin.readline
from heapq import heappop,heappush

n,m,H = map(int,input().split())

inf = 10**20

AB = [list(map(int,input().split())) for i in range(n)]

attacks = [0]*(m+1)

ink = [0]*m

strongH = []

mod = 1<<20
heappush(strongH,(inf<<20) + m)
attacks[-1] = inf
weakH = []
for i in range(m):
    heappush(weakH,-i)

now = 0
ans = [0]*(m+1)
damages = 0

size = 0
for i in range(n):
    
    a,b = AB[i]
    b -= 1

    attacks[b] += a

    if ink[b]:
        heappush(strongH,(attacks[b]<<20)+b)
        continue

    damages += a
    heappush(weakH,-((attacks[b]<<20)+b))
    while weakH:
        wmax,wb = divmod(-weakH[0],mod)
        if attacks[wb] != wmax:
            heappop(weakH)
        else:
            break

    while strongH:
        smin,sb = divmod(strongH[0],mod)
        if attacks[sb] != smin:
            heappop(strongH)
        else:
            break

    if wmax > smin:

        damages += smin-wmax
        ink[wb] = 1
        ink[sb] = 0

        heappop(strongH)
        heappop(weakH)

        heappush(strongH,(wmax<<20)+wb)
        heappush(weakH,-((smin<<20)+sb))

    
    if damages < H:
        continue

    while damages >= H:
        ans[size] = i
        while weakH:
            wmax,wb = divmod(-weakH[0],mod)
            if attacks[wb] != wmax:
                heappop(weakH)
            else:
                break
        
        damages -= wmax
        ink[wb] = 1
        size += 1
        heappop(weakH)
        heappush(strongH,(wmax<<20)+wb)        

for i in range(size,m+1):
    ans[i] = n
print(*ans)