t = int(input())
for _ in range(t):
    l,r = map(int,input().split())
    x = max(r-2*l+1,0)
    print(x*(x+1)//2)