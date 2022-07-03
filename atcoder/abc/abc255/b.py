n,k = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for i in range(n)]


def solve(R):
    light = [0]*n
    for a in A:
        x,y = XY[a-1]
        for i in range(n):
            nx,ny = XY[i]
            if (x-nx)**2 + (y-ny)**2 <= R**2:
                light[i] = 1

    return sum(light) == n
l = 0
r = 10**7

for i in range(50):
    m = (r+l)/2
    if solve(m):
        r = m
    else:
        l = m
print(l)
