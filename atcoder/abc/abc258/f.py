def manhattan(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def move(x,y,id,b,k):
    if id%2:
        nx = (x//b+id//2)*b
        ny = y
    else:
        nx = x
        ny = (y//b+id//2)*b
    
    cost = manhattan(x,y,nx,ny)*k
    return nx,ny,cost

def move2(si,sj,gi,gj,b):

    if si%b:
        si,sj = sj,si
        gi,gj = gj,gi

    dis = manhattan(si,sj,gi,gj)
    if gi%b:
        return dis
    if sj//b != gj//b:
        return dis
    if si == gi:
        return dis

    c1 = sj%b + gj%b

    return abs(si-gi)+min(c1,2*b-c1)
def solve():
    b,k,sx,sy,gx,gy = map(int,input().split())

    ans = manhattan(sx,sy,gx,gy)*k

    for i in range(4):
        for j in range(4):

            si,sj,cost = move(sx,sy,i,b,k)
            gi,gj,cost2 = move(gx,gy,j,b,k)

            count = cost+cost2
            count += move2(si,sj,gi,gj,b)
            ans = min(ans,count)

    print(ans)

t = int(input())
for _ in range(t):
    solve()



