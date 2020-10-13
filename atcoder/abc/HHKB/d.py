t = int(input())
mod = 10**9+7

for _ in range(t):
    n,a,b = map(int,input().split())
    ans = 0
    if n >= a+b:
        d = n-a-b+1
        x = d*(d+1)
        y = (n-a+1)*(n-b+1)-x
        ans = (n-a+1)**2*(n-b+1)**2-y**2
    print(ans%mod)

