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
                if m < mo*mo*sp:
                    ind = i
                    m = mo*mo*sp
        
        if ind == -1:
            break
        ans.append(S[ind])
        x = x+dx[ind]
        y = y+dy[ind]
        vis[x][y] = 1
        use[T[x][y]] = 1
        dis.append([x,y])

def searchrandom(sx,sy):
    x = sx
    y = sy
    while True:
        cand = []
        ma = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] == 0 and T[x][y] != T[nx][ny] and use[T[nx][ny]] == 0:
                mo = move(nx,ny,x,y)
                if mo == 0:
                    continue
                cand.append([mo,i])
                ma += mo
        
        if cand == []:
            break
        
        rand = random.randint(0,ma-1)
        now = 0
        for j,i in cand:
            if now <= rand < now+j:
                ind = i
                break
            now += j

        ans.append(S[ind])
        x = x+dx[ind]
        y = y+dy[ind]
        vis[x][y] = 1
        use[T[x][y]] = 1
        dis.append([x,y])
searchgreed(si,sj)
bestscore = get_score(dis)
bestans = deepcopy(ans)
bestdis = deepcopy(dis)
bestvis = deepcopy(vis)
bestuse = deepcopy(use)

while time.time()-start < 1.82:
    le = len(bestans)
    srand = random.randint(1,le-1)
    ans = bestans[:srand-1]
    dis = bestdis[:srand]
    for x,y in bestdis[srand:]:
        vis[x][y] = 0
        use[T[x][y]] = 0

    searchrandom(dis[-1][0],dis[-1][1])
    nscore = get_score(dis)
    if nscore > bestscore:
        bestscore = nscore
        bestans = deepcopy(ans)
        bestdis = deepcopy(dis)
        bestvis = deepcopy(vis)
        bestuse = deepcopy(use)
    else:
        vis = deepcopy(bestvis)
        use = deepcopy(bestuse)
print(*bestans,sep="")
