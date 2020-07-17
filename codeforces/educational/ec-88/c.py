T = int(input())

for _ in range(T):
    h,c,t = map(int,input().split())
    if h+c >= 2*t:
        print(2)
    else:
        x = (h-t)//(2*t-c-h)
        y = x+1
        if abs(h*(x+1)+c*x-t*(2*x+1))*(2*y+1) <= abs(h*(y+1)+c*y-t*(2*y+1))*(2*x+1):
            print(2*x+1)
        else:
            print(2*y+1)
        