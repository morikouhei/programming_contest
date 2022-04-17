import random
from collections import deque
from heapq import heappush,heappop

si,sj,ti,tj,p = input().split()
si,sj,ti,tj = int(si),int(sj),int(ti),int(tj)
p = float(p)
Ti,Tj = ti,tj
H = [list(map(int,input())) for i in range(20)]
V = [list(map(int,input())) for i in range(19)]

M = 20
lim = 200



movedic = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}

def canMove(x,y,move_s):

    dx,dy = movedic[move_s]
    nx = dx + x
    ny = dy + y

    if nx < 0 or nx >= M or ny < 0 or ny >= M:
        return -1,-1

    if move_s == "U":
        if V[nx][ny]:
            return -1,-1

    if move_s == "D":
        if V[x][y]:
            return -1,-1


    if move_s == "R":
        if H[x][y]:
            return -1,-1

    if move_s == "L":
        if H[nx][ny]:
            return -1,-1
    
    return nx,ny



dis = [[lim*5]*M for i in range(M)]
dis[si][sj] = 0
q = []
heappush(q,[0,si,sj])
record = [[0]*M for i in range(M)]
while q:
    dd,x,y = heappop(q)
    if dis[x][y] != dd:
        continue

    for move_s in "UDLR":
        nx,ny = x,y
        while True:

            nnx,nny = canMove(nx,ny,move_s)
            if nnx == -1:
                break
            nx,ny = nnx,nny
            if nnx == ti and nny == tj:
                break
            
        d = abs(x-nx)+abs(y-ny)
        if dis[nx][ny] > dd + d:
            dis[nx][ny] = dd + d
            heappush(q,[dd+d,nx,ny])
            record[nx][ny] = [x,y]

dis2 = [[lim*5]*M for i in range(M)]
dis2[ti][tj] = 0
q = deque()
q.append([ti,tj])
while q:
    x,y = q.popleft()
    for move_s in "UDLR":
        nx,ny = canMove(x,y,move_s)

        if nx != -1 and dis2[nx][ny] > dis2[x][y]+1:
            dis2[nx][ny] = dis2[x][y] + 1
            q.append([nx,ny])


if record[ti][tj] == 0:

    nnx,nny = -1,-1
    dist = 10**10
    dist2 = 10**10
    for i in range(M):
        for j in range(M):
            if record[i][j] == 0:
                continue
            
            if dis2[i][j] <= 10:
                d = dis2[i][j] * dis[i][j]
                if d < dist:
                    dist = d
                    nnx,nny = i,j
            elif dis2[i][j] <= 20:
                d = dis2[i][j] * dis[i][j]
                if d < dist2:
                    dist2 = d
                    nnx2,nny2 = i,j


    ti,tj = nnx,nny
    if ti == -1:
        ti,tj = nnx2,nny2


nowx,nowy = ti,tj
path = []
dist = 0
while True:
    if nowx == si and nowy == sj:
        break
    bx,by = record[nowx][nowy]
    d = abs(bx-nowx)+abs(by-nowy)
    dist += d
    if bx < nowx:
        path.append(["D",d])
    elif bx > nowx:
        path.append(["U",d])
    elif by < nowy:
        path.append(["R",d])
    else:
        path.append(["L",d])
    nowx,nowy = bx,by
path = path[::-1]
l = dist
m = lim//l
if Ti != ti or Tj != tj:
    m = max(0,m-1)
ans = []
for s,d in path:
    dp = [0]*(d+1)
    dp[0] = 1
    for i in range(d*m):
        ans.append(s)
        ndp = [0]*(d+1)
        for j in range(d+1):
            if j == d:
                ndp[j] += dp[j]
                continue

            ndp[j] += dp[j]*p
            ndp[j+1] += dp[j]*(1-p)
        dp = ndp
        if dp[-1] >= 0.98:
            break
if ti == Ti and tj == Tj:
    ss = "UDLR"
    for i in range(len(ans),lim):
        s = random.randint(0,3)
        ans.append(ss[s])

    

else:

    turn = lim-len(ans)

    prob = [[0]*M for i in range(M)]
    prob[ti][tj] = 1

    for _ in range(turn):

        dic = {"U":0,"D":0,"L":0,"R":0}

        for i in range(M):
            for j in range(M):
                if i == Ti and j == Tj:
                    continue
                cand = []
                for move_s in "UDLR":
                    nx,ny = canMove(i,j,move_s)
                
                    if nx != -1 and dis2[nx][ny] == dis2[i][j]-1:
                        cand.append(move_s)
                if cand == []:
                    continue
                if len(cand) == 1:
                    dic[cand[0]] += prob[i][j]*(100-dis2[i][j])
                else:
                    dic[cand[0]] += prob[i][j]/2*(100-dis2[i][j])
                    dic[cand[1]] += prob[i][j]/2*(100-dis2[i][j])
        p2 = 0
        dist = "U"
        count = 0
        for s,v in dic.items():
            count += v
            if p2 < v:
                p2 = v
                dist = s

        if count >= p2*2:
            if random.randint(1,10) <= 6:
                x = random.randint(0,3)
                dist = "UDLR"[x]
        nprob = [[0]*M for i in range(M)]
        for i in range(M):
            for j in range(M):
                if i == Ti and j == Tj:
                    continue
                nx,ny = canMove(i,j,dist)
                if nx != -1:
                    nprob[nx][ny] += prob[i][j]*(1-p)
                    nprob[i][j] += prob[i][j]*p
                else:
                    nprob[i][j] += prob[i][j]
        prob = nprob
        ans.append(dist)

            
print("".join(ans))