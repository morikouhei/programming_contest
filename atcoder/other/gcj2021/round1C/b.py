def check(x,ma):
    if x > ma:
        return 10**40
    now = str(x)
    c1 = x
    while int(now) <= ma:
        c1 += 1
        now += str(c1)
    return int(now)

def solve():
    n = int(input())
    ans = 10**40
    for i in range(1,20):
        x = 10**i
        for j in range(1,10):
            ans = min(ans,check(x-j,n))
    for i in range(1,len(str(n))):
        cand = str(n)[:i]
        for j in range(10):
            ans = min(ans,check(int(cand)+j,n))
    
    
    return ans
T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))