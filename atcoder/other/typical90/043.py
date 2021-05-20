from collections import deque
h,w = map(int,input().split())
rs,cs = [int(i)-1 for i in input().split()]
rt,ct = [int(i)-1 for i in input().split()]

C = [input() for i in range(h)]
inf = 10**6
M = h*w*4
dp = [inf]*M
mod = 1<<32

def to_id(x,y,t):
    return t*h*w+x*w+y

def to_pos(id):
    t,num = divmod(id, h*w)
    x,y = divmod(num, w)
    return x,y,t

q = deque([])
for i in range(4):
    id = to_id(rs,cs,i)
    dp[id] = 0
    q.append(id)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

while q:
    d,id = divmod(q.popleft(),mod)
    x,y,ind = to_pos(id) 
    if dp[id] != d:
        continue
    if x == rt and y == ct:
        print(d)
        exit()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 > nx or 0 > ny or nx >= h or ny >= w or C[nx][ny] == "#":
            continue

        nid = to_id(nx, ny, i)
        if i == ind:
            if dp[nid] > d:
                dp[nid] = d
                q.appendleft(nid+(d<<32))
            continue
        if dp[nid] > d+1:
            dp[nid] = d+1
            q.append(nid+((d+1)<<32))
