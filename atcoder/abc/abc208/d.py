n,m = map(int,input().split())
inf = 10**20
e = [[inf]*n for i in range(n)]
for _ in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    e[a][b] = c
for i in range(n):
    e[i][i] = 0
ans = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if e[i][j] > e[i][k]+e[k][j]:
                e[i][j] = e[i][k]+e[k][j]
            if e[i][j] != inf:
                ans += e[i][j]
print(ans)