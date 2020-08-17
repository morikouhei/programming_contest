t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ma = min(a)
    mb = min(b)
    ans = 0
    for i,j in zip(a,b):
        if i > ma and j > mb:
            x = min(i-ma,j-mb)
            i -= x
            j -= x
            ans += x + (i-ma)+(j-mb)
        elif i > ma:
            ans += i-ma
        elif j > mb:
            ans += j-mb
        
    print(ans)