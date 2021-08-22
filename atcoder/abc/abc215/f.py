n = int(input())
XY = [tuple(map(int,input().split())) for i in range(n)]
XXY = sorted(XY)
def search(ans):
    mi = 10**10
    ma = -10**10
    now = 0
    for i,(x,y) in enumerate(XXY):
        while now < i and x-XXY[now][0] >= ans:
            ny = XXY[now][1]
            mi = min(mi,ny)
            ma = max(ma,ny)
            now += 1
        if ma-y >= ans:
            return True
        if y-mi >= ans:
            return True

    
    return False

l = 0
r = 10**9+5
while r > l+1:
    m = (r+l)//2
    if search(m):
        l = m
    else:
        r = m
print(l)