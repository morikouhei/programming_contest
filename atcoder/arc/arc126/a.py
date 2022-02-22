
def solve():
    ans = 0
    n2,n3,n4 = map(int,input().split())
    n6 = n3//2

    m = min(n6,n4)
    ans += m
    n6 -= m
    n4 -= m

    m = min(n6,n2//2)
    ans += m
    n6 -= m
    n2 -= 2*m
    
    m = min(n4//2,n2)
    ans += m
    n4 -= m*2
    n2 -= m

    m = min(n4,n2//3)
    ans += m
    n4 -= m
    n2 -= 3*m
    ans += n2//5
    return ans

t = int(input())
for _ in range(t):
    print(solve())