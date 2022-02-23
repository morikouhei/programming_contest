import sys
input = sys.stdin.readline

def solve():
    n,m = map(int,input().split())
    XY = [list(map(int,input().split())) for i in range(n)]
    ans = -10**20
    A = 0
    B = 0
    def f(x,c):
        count = A + x*B + x*(x+1)//2 * c
        return count

    for x,y in XY:
        lp = 0 if x == 0 else -(2*B+x)//(2*x)
        rp = lp+1
        ans = max(ans,f(1,x))
        ans = max(ans,f(y,x))
        if 0 < lp < y:
            ans = max(ans,f(lp,x))
        if 0 < rp < y:
            ans = max(ans,f(rp,x))
        A = f(y,x)
        B += x*y
    
    return ans


t = int(input())
for _ in range(t):
    print(solve())