t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    x = min(m,n//k)
    if n//k >= m:
        print(m)
    else:
        m -= n//k
        x = (m+k-2)//(k-1)
        print(n//k-x)