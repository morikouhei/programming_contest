n,m = map(int,input().split())

if (n+1)**2 < m:
    print(-1)
    exit()

ans = 10**20
for a in range(1,10**7):
    if a > n:
        break

    b = (m+a-1)//a

    if b > n:
        continue
    if a*b >= m:
        ans = min(ans,a*b)

if ans == 10**20:
    ans = -1
print(ans)
