n = int(input())
X = list(map(int,input()))
mod = 998244353

count = 0
ans = 0
for i,x in enumerate(X):
    ans += count*x
    count *= 10
    count += x*pow(2,i,mod)
    count %= mod
print(ans+count)