def solve():
    a,b = map(int,input().split())
    if b <= a:
        return abs(a-b)

    ans = abs(a-b)

    for i in range(10**5):
        x = a+i
        y = (x-b%x)%x
        ans = min(ans,i+y)

    
    for i in range(1,10**5):
        if b <= i*a:
            ans = min(ans,i*a-b)
        else:
            x = (b+i-1)//i-a
            y = (a+x)*i-b
            ans = min(ans,x+y)
    

    return ans

t = int(input())
for _ in range(t):
    print(solve())