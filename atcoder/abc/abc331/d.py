n,q = map(int,input().split())
P = [input() for i in range(n)]

nums = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if P[i][j] == "B":
            nums[i][j] = 1

for i in range(n):
    for j in range(n-1):
        nums[i][j+1] += nums[i][j]

for i in range(n-1):
    for j in range(n):
        nums[i+1][j] += nums[i][j]


def get(x,y):
    if x < 0 or y < 0:
        return 0

    lx = x//n
    ly = y//n
    base = lx*ly*nums[-1][-1]


    mx,my = x%n,y%n
    base += ly * nums[mx][-1]
    base += lx * nums[-1][my]

    base += nums[mx][my]
    
    return base

ABCD = [list(map(int,input().split())) for i in range(q)]

for a,b,c,d in ABCD:

    ans = get(c,d) + get(a-1,b-1) - get(c,b-1) - get(a-1,d)

    print(ans)