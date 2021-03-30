h,w,x,y = map(int,input().split())
S = [list(input()) for i in range(h)] 
x -= 1
y -= 1
ans = 1
for i,j in ((0,1),(1,0),(0,-1),(-1,0)):
    nx = x + i
    ny = y + j
    while 0 <= nx < h and 0 <= ny < w and S[nx][ny] == ".":
        ans += 1
        nx += i
        ny += j
print(ans)