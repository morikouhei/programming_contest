n,t,l = map(int,input().split())
inf = 10**5
g = [[inf]*n for i in range(n)]

for i in range(t):
    u,v = [int(x)-1 for x in input().split()]
    g[u][v] = i+1

def calc(A,B):
    ans = [[inf]*n for i in range(n)]
    for i in range(n):   
        for j in range(n):
            for k in range(n):
                ans[i][j] = min(ans[i][j],max(A[i][k],B[k][j]))

    return ans


base = [[inf]*n for i in range(n)]
for i in range(n):
    base[i][i] = 0

while l:
    if l&1:
        base = calc(base,g)
    g = calc(g,g)
    l >>= 1

ans = [-1]*n
for i in range(n):
    if base[0][i] != inf:
        ans[i] = base[0][i]
print(*ans)