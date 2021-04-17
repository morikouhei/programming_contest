n,p = map(int,input().split())
mod = 10**9+7
ans = (p-1)*pow(p-2,n-1,mod)
print(ans%mod)