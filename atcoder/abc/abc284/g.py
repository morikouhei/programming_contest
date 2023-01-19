n,mod = map(int,input().split())

ans = 0

def nC2(x):
    return x*(x-1)//2
perm = n
for l in range(1,n+1):
    ans += pow(n,n-l,mod)*nC2(l)*perm%mod
    ans %= mod

    perm *= (n-l)
    perm %= mod
print(ans)