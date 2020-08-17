import sys

n = int(input())

l = [[0]*n for i in range(n)]

for i in range(n):
    if i%2 == 0:
        continue
    for j in range(n):
        l[i][j] = pow(2,i+j+2)

for i in l:
    print(*i)
    sys.stdout.flush()
q = int(input())
for _ in range(q):
    s = int(input())
    nx = 0
    ny = 0
    for i in range(2*n-1):
        print(nx+1,ny+1)
        sys.stdout.flush()
        if nx%2 == 0:
            if s & pow(2,nx+3+ny):
                nx += 1
            else:
                ny += 1
        else:
            if s & pow(2,nx+ny+3):
                ny += 1
            else:
                nx += 1
