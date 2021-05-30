from collections import deque
h,w = map(int,input().split())
dic = {"R":0, "B":1, ".":2}
S = [[dic[i] for i in input()] for j in range(h)]
mod = 998244353

ans = 1
dis = [[0]*3 for i in range(h+w+5)]
d = [[h*w+5]*w for i in range(h)]

d[0][0] = 0

q = deque([[0,0]])
while q:
    x,y = q.popleft()
    dis[d[x][y]][S[x][y]] += 1

    for i,j in ((-1,0),(0,-1),(1,0),(0,1)):
        nx = x+i
        ny = y+j
        if 0 <= nx < h and 0 <= ny < w and d[nx][ny] > d[x][y]+1:
            d[nx][ny] = d[x][y]+1
            q.append([nx,ny])

for x,y,z in dis:
    if x != 0 and y != 0:
        ans *= 0
        continue
    if x == y == 0 and z != 0:
        ans *= 2
        ans %= mod
print(ans)