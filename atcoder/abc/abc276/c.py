n = int(input())
P = list(map(int,input().split()))
last = n+1
for i in range(n)[::-1]:
    if last > P[i]:
        last = P[i]
    else:
        sP = sorted(P[i:])
        np = sP[sP.index(P[i])-1]
        sP.remove(np)

        ans = P[:i]+[np] + sP[::-1]
        print(*ans)
        exit()
