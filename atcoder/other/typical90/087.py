n,p,k = map(int,input().split())
dis = [list(map(int,input().split())) for i in range(n)]


def search(x):
    d = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if dis[i][j] == -1:
                d[i][j] = x
            else:
                d[i][j] = dis[i][j]

    for m in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][m]+d[m][j])
    count = 0
    for i in range(n):
        for j in range(i):
            if d[j][i] <= p:
                count += 1
    return count
l = 0
r = 10**9+5
while r > l+1:
    m = (r+l)//2
    if search(m) < k:
        r = m
    else:
        l = m
l2 = 0
r2 = 10**9+5
while r2 > l2+1:
    m = (r2+l2)//2
    if search(m) <= k:
        r2 = m
    else:
        l2 = m

if r == 10**9+5:
    if r2 == 10**9+5:
        print(0)
    else:
        print("Infinity")
else:
    print(r-r2)

