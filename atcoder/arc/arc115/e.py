n = int(input())
A = list(map(int,input().split()))
mod = 998244353

ans = 0
now = 1
for a in A:
    now *= a
    now %= mod
ans += now

for i in range(n-1):
    for j in range(i+1,n):
        mi = 10**20
        print(i,j)
        for k in range(i,j+1):
            mi = min(mi,A[k])
        check = True
        base = now
        print(base,mi)
        for k in range(i,j+1):
            if A[k] == mi and check == True:
                check = False
                continue
            base *= pow(A[k],mod-2,mod)
            base %= mod
        print(base)
        if (j-i)%2:
            ans -= base
        else:
            ans += base
        ans %= mod
print(ans)