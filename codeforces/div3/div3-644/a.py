t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    print(max(a,b*2)**2)