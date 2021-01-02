n = int(input())
ab = [list(map(int,input().split())) for i in range(n)]
ab.sort(key = lambda x: (2*x[0]+x[1]),reverse=True)
s = 0
for a,b in ab:
    s += a

ans = 0
for i in range(n):
    a,b = ab[i]
    ans += a*2+b
    if ans > s:
        print(i+1)
        exit() 