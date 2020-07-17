t = int(input())
for _ in range(t):
    x,y,n = map(int,input().split())
    k = (n-y)//x
    print(k*x+y)