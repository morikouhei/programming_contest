n,m,k = map(int,input().split())
A = list(map(int,input().split()))
e = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
mod = 10**9+7
mat = [[0]*n for i in range(n)]
for i in range(n):
    d = len(e[i])
    pro = d*pow(2*m,mod-2,mod)
    mat[i][i] = (1-pro)%mod
    for j in e[i]:
        mat[j][i] = pow(2*m,mod-2,mod)


base = [[0]*n for i in range(n)]
for i in range(n):
    base[i][i] = 1

def calc(a,b):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += a[i][k]*b[k][j]
                C[i][j] %= mod
    return C

while k:
    if k%2:
        base = calc(base,mat)
    mat = calc(mat,mat)
    k //= 2

for i in range(n):
    ans = 0
    for j in range(n):
        ans += base[j][i]*A[j]
        ans %= mod
    print(ans)