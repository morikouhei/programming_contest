n,m = map(int,input().split())
mod = 998244353



def calc(x,y):
    if x == 0 or y == 0:
        return 0

    
    num = x//2

    base = (y*(y+1)//2)*num
    if x%2:
        num = (y+1)//2
        l = 1
        r = 1 + (num-1)*2
        base += (l+r)*num//2
    base %= mod
    
    num = (x+1)//2
    a = (y+1)//2
    l = 0
    r = (num-1)*2

    base += (l+r)*num//2*(a*m)%mod
    base %= mod
    num = x//2
    a = y//2

    l = 1
    r = 1 + (num-1)*2

    base += (l+r)*num//2*(a*m)%mod

    base %= mod

    return base

def solve():
    a,b,c,d = map(int,input().split())
    a -= 1
    c -= 1
    ans = calc(b,d)-calc(b,c)-calc(a,d)+calc(a,c)

    return ans%mod


q = int(input())
for _ in range(q):
    print(solve())