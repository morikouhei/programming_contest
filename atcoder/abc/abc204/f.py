h,w = map(int,input().split())
mod = 998244353
n = 1<<h
def prod(a,b):
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += a[i][k]*b[k][j]
                ans[i][j] %= mod
    return ans

ans = [[0]*n for i in range(n)]
for i in range(n):
    ans[i][i] = 1

fib = [1,1,2,3,5,8,13,21]
base = [[0]*n for i in range(n)]
mask = n-1
for i in range(n):
    need = mask & (~i)
    for j in range(n):
        if j&need != j:
            continue
        new = j^need
        count = 1
        num = 0
        for k in range(h+1):
            if new >> k & 1:
                num += 1
            else:
                count *= fib[num]
                num = 0
        base[i][j] = count%mod

while w:
    if w%2:
        ans = prod(ans,base)
    base = prod(base,base)
    w //= 2
print(ans[0][0])
        
