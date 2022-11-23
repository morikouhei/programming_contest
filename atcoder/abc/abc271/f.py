n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

dic = {}

for i in range(1<<n-1):

    x,y = 0,0
    now = A[0][0]
    for j in range(n-1):
        if i >> j & 1:
            y += 1
        else:
            x += 1
        now ^= A[x][y]
    dic[(x*n+y,now)] = dic.get((x*n+y,now),0)+1

ans = 0
for i in range(1<<n-1):
    x,y = n-1,n-1
    now = A[-1][-1]
    for j in range(n-1):
        if i >> j & 1:
            y -= 1
        else:
            x -= 1
        now ^= A[x][y]
    now ^= A[x][y]
    if (x*n+y,now) in dic:
        ans += dic[(x*n+y,now)]
    # dic[(x*n+y,now)] = dic.get((x+n+y,now),0)+1
print(ans)