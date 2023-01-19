n,m = map(int,input().split())
mod = 998244353
print(pow(n,m,mod)*pow(m,n-1,mod)%mod)