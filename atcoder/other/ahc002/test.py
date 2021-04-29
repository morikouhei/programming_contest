import time
import random
from copy import deepcopy
start = time.time()
si,sj = map(int,input().split())
n = 50
T = [list(map(int,input().split())) for i in range(n)]
P = [list(map(int,input().split())) for i in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
S = "RLDU"

def move(x,y,bx,by):
    count = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx == bx and ny == by:
            continue
        if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] == 0 and T[x][y] != T[nx][ny] and use[T[nx][ny]] == 0:
            count += 1
    return count

def space(x,y,ind):
    count = 0
    if ind == 0:
        l,r = y,y+7
        u,d = x-3,x+4
    if ind == 1:
        l,r = y-6,y+1
        u,d = x-3,x+4
    if ind == 2:
        l,r = y-3,y+4
        u,d = x,x+7
    if ind == 3:
        l,r = y-3,y+4
        u,d = x-6,x+1

    for i in range(u,d):
        for j in range(l,r):
            if 0 <= i < n and 0 <= j < n and vis[i][j] == 0  and use[T[i][j]] == 0:
                count += 1
    return count

def get_score(dis):
    count = 0
    for x,y in dis:
        count += P[x][y]
    return count

use = [0]*2505
ans = []
dis = [[si,sj]]
vis = [[0]*n for i in range(n)]
vis[si][sj] = 1
use[T[si][sj]] = 1

def searchgreed(sx,sy):
    x = sx
    y = sy
    while True:
        
        ind = -1
        m = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] == 0 and T[x][y] != T[nx][ny] and use[T[nx][ny]] == 0:
                mo,sp = move(nx,ny,x,y),space(nx,ny,i)
                if m < mo*sp:
                    ind = i
                    m = mo*sp
        
        if ind == -1:
            break
        ans.append(S[ind])
        x = x+dx[ind]
        y = y+dy[ind]
        vis[x][y] = 1
        use[T[x][y]] = 1
        dis.append([x,y])
searchgreed(si,sj)
bestscore = get_score(dis)
bestans = ans
bestdis = dis
bestvis = vis
bestuse = use
while time.time()-start < 1.8:
    le = len(bestans)
    rand = random.randint(1,le//2)
    ans = bestans[:rand-1]
    dis = bestdis[:rand]
    for x,y in bestdis[rand:]:
        vis[x][y] = 0
        use[T[x][y]] = 0

    searchgreed(dis[-1][0],dis[-1][1])
    nscore = get_score(dis)
    if nscore > bestscore:
        bestscore = nscore
        bestans = ans
        bestdis = dis
        bestvis = vis
        bestuse = use
    else:
        vis = deepcopy(bestvis)
        use = deepcopy(bestuse)
print(*ans,sep="")


