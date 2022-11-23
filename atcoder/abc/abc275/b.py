a,b,c,d,e,f = map(int,input().split())
ans = a*b*c - d*e*f
print(ans%998244353)