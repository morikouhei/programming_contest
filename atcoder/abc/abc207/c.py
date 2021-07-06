n = int(input())
ans = 0
L = [list(map(int,input().split())) for i in range(n)]

def ran(x):
    t,l,r = L[x]
    l *= 2
    r *= 2
    if t == 1:
        return l,r
    elif t == 2:
        return l,r-1
    elif t == 3:
        return l+1,r
    else:
        return l+1,r-1
for i in range(n):
    for j in range(i):
        x,y = ran(i)
        nx,ny = ran(j)
        if x <= nx <= y or x <= ny <= y or nx <= x <= ny or nx <= y <= ny:
            ans += 1
print(ans)