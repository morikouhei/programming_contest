t = int(input())
for _ in range(t):
    n,m,x = map(int,input().split())
    a,b = divmod(max(0,x-1),n)
    print(b*m+a+1)
