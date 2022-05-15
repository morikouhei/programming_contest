from collections import deque

M = 30
T = [list(map(int,input())) for i in range(M)]

ans = [[0]*M for i in range(M)]
### lane 0 - 3 change to 0
### lane 4,5 change to 4
### lane 6,7 changet to 6
for i in range(M):
    for j in range(M):
        t = T[i][j]
        if 0 <= t <= 3:
            ans[i][j] = (4-t)%4
            T[i][j] = 0

        if t == 5:
            ans[i][j] = 1
            T[i][j] = 4
        if t == 7:
            ans[i][j] = 1
            T[i][j] = 6


locked = [[0]*M for i in range(M)]


def rotate(x,y,d):
    t = T[x][y]
    if 0 <= t <= 3:
        T[x][y] += d
        T[x][y] %= 4
        

    if 4 <= t <= 5:
        if d%2:
            if t == 4:
                T[x][y] = 5
            else:
                T[x][y] = 4

    if 6 <= t <= 7:
        if d%2:
            if t == 6:
                T[x][y] = 7
            else:
                T[x][y] = 6
            
    ans[x][y] += d
    ans[x][y] %= 4

def is_in(x,y):
    if x < 0 or x >= M or y < 0 or y >= M:
        return False

    return True


dx = [0,-1,0,1]
dy = [-1,0,1,0]

to = [
    [1, 0, -1, -1],
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [2, -1, 0, -1],
    [-1, 3, -1, 1],
]

def count_loop(si,sj,sd):
    i = si
    j = sj
    d = sd
    locked[si][sj] = 1
    length = 0
    while True:
        d2 = to[T[i][j]][d];

        if d2 == -1:
            return 0

        i += dx[d2]
        j += dy[d2]
        length += 1
        if is_in(i,j) == False:
            return 0

        

        d = (d2 + 2) % 4
        if i == si and j == sj and d == sd:
            return length 
        locked[i][j] = 1
    return 0


def bfs(x,y):
    lane = T[x][y]
    if 6 <= lane:
        return -1,(-1)

    x1,y1 = x+dx[0],y+dy[0]

    if is_in(x1,y1) == False:
        return -1,(-1)

    if T[x1][y1] != 4 and T[x1][y1] != 6:
        return -1,(-1)

    x2,y2 = x+dx[3],y+dy[3]

    if is_in(x2,y2) == False:
        return -1,(-1)

    if T[x2][y2] != 0 and T[x2][y2] != 4:
        return -1,(-1)

    
    vis = [[[-1]*4 for i in range(M)] for j in range(M)]
    length = -1
    tx,ty = -1,-1

    vis[x1][y1][2] = 1
    vis[x2][y2][1] = 1
    q = deque([])
    q.append((x1,y1,2,1))
    q.append((x2,y2,1,1))

    while q:
        nx,ny,d,l = q.popleft()
        t = T[nx][ny]

        if t == 0:
            if d != 1:
                continue
            nnx,nny = nx+dx[0],ny+dy[0]

            if is_in(nnx,nny) == False:
                continue

            nt = T[nnx][nny]
            if nt == 0 or nt == 4:
                if vis[nnx][nny][1] > 0:
                    if length < vis[nnx][nny][1]:
                        length = vis[nnx][nny][1]
                        tx,ty = nnx,nny

            if vis[nnx][nny][2] > 0:
                continue

            if nt == 4 or nt == 6:
                vis[nnx][nny][2] = l+1
                q.append((nnx,nny,2,l+1))


        if t == 4:
            if d == 1:
    
                nnx,nny = nx+dx[0],ny+dy[0]

                if is_in(nnx,nny) == False:
                    continue

                nt = T[nnx][nny]
                if nt == 0 or nt == 4:
                    if vis[nnx][nny][1] > 0:
                        if length < vis[nnx][nny][1]:
                            length = vis[nnx][nny][1]
                            tx,ty = nnx,nny

                if vis[nnx][nny][2] > 0:
                    continue

                if nt == 4 or nt == 6:
                    vis[nnx][nny][2] = l+1
                    q.append((nnx,nny,2,l+1))

            elif d == 2:

                nnx,nny = nx+dx[3],ny+dy[3]

                if is_in(nnx,nny) == False:
                    continue

                nt = T[nnx][nny]
                if nt == 0 or nt == 4:
                    if vis[nnx][nny][2] > 0:
                        if length < vis[nnx][nny][2]:
                            length = vis[nnx][nny][2]
                            tx,ty = nnx,nny

                if vis[nnx][nny][1] > 0:
                    continue

                if nt == 0 or nt == 4:
                    vis[nnx][nny][1] = l+1
                    q.append((nnx,nny,1,l+1))

        if t == 6:
            if d != 2:
                continue
            nnx,nny = nx+dx[0],ny+dy[0]

            if is_in(nnx,nny) == False:
                continue

            nt = T[nnx][nny]
            if nt == 0 or nt == 4:
                if vis[nnx][nny][1] > 0:
                    if length < vis[nnx][nny][1]:
                        length = vis[nnx][nny][1]
                        tx,ty = nnx,nny

            if vis[nnx][nny][2] > 0:
                continue

            if nt == 4 or nt == 6:
                vis[nnx][nny][2] = l+1
                q.append((nnx,nny,2,l+1))

    return length,(x,y,tx,ty)

lmax = []
point = []
for i in range(M):
    for j in range(M):
        nl,cand = bfs(i,j)
        lmax.append([nl,len(lmax)])
        point.append(cand)


lmax.sort(reverse=True)
for i in range(2):
    _,ind = lmax[i]
    x,y,tx,ty = point[ind]
    rotate(x,y,1)
    # print(T[x][y])
    rotate(tx,ty,3)
    # print(T[tx][ty])
    print(x,y,tx,ty)
    print(count_loop(x,y,3))

# print(lmax)












### output
for i in ans:
    print(*i,sep="",end="")
