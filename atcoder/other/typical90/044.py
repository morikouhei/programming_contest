n,q = map(int,input().split())
A = list(map(int,input().split()))
now = 0
for i in range(q):
    s,x,y = [int(t)-1 for t in input().split()]
    if s == 0:
        A[(x+now)%n],A[(y+now)%n] = A[(y+now)%n],A[(x+now)%n]
    elif s == 1:
        now -= 1
    else:
        print(A[(x+now)%n])
