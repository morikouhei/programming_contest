n,k = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
l = -1
r = 10**9+5
need = (k**2)//2+1
def check(x):
    cum = [[0]*(n+1) for i in range(n+1)]
    for i in range(n):
        for j in range(n):
            if A[i][j] >= x:
                cum[i+1][j+1] = 1

    for i in range(1,n+1):
        for j in range(1,n+1):
            cum[i][j] += cum[i-1][j]+cum[i][j-1]-cum[i-1][j-1]
    
    for i in range(k,n+1):
        for j in range(k,n+1):
            if cum[i][j]+cum[i-k][j-k]-cum[i-k][j]-cum[i][j-k] < need:
                return True
    return False

while r > l + 1:
    m = (r+l)//2
    if check(m):
        r = m
    else:
        l = m

print(l)