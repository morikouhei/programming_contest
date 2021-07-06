l,r = map(int,input().split())
def count(x):
    ans = 0
    bef = 0
    now = 1
    for i in range(1,20):
        now *= 10
        m = min(now-1,x)
        ans += i*((m*(m+1)//2-bef*(bef+1)//2))
        if m == x:
            return ans
        bef = now-1
print((count(r)-count(l-1))%(10**9+7))