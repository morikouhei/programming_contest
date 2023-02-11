import time
import random
import sys
from collections import deque
input = sys.stdin.readline

stime = time.time()
TIME_LIM = 6
inf = 10**9

center = 1000
SPLIT = 10

n,m,d,k = map(int,input().split())

UVW = [list(map(int,input().split())) for i in range(m)]
UVW = [[u-1,v-1,w] for u,v,w in UVW]
XY = [list(map(int,input().split())) for i in range(n)]

g = [[] for i in range(n)]
for i,(u,v,w) in enumerate(UVW):
    g[u].append((v,w,i))
    g[v].append((u,w,i))

xma = [-inf,-1]
xmi = [inf,-1]
yma = [-inf,-1]
ymi = [inf,-1]

for i,(x,y) in enumerate(XY):
    if xma[0] < x:
        xma = [x,i]
    if xmi[0] > x:
        xmi = [x,i]
    
    if yma[0] < y:
        yma = [y,i]
    if ymi[0] > y:
        ymi = [y,i]
    

dist_point = set([xma[1],xmi[1],yma[1],ymi[1]])
dist_point = set([xma[1],xmi[1]])

def dist_sum(used,day=1):
    
    dist_count = 0
    for i in dist_point:
        dist = [inf]*n
        dist[i] = 0
        q = deque([i])
        while q:
            now = q.popleft()
            for nex,w,id in g[now]:
                if used[id]:
                    continue
                if dist[nex] > dist[now]+w:
                    dist[nex] = dist[now]+w
                    q.append(nex)
        dist_count += sum(dist)

    return dist_count

def pos_split_R():


    nXY = [[x*2-center,y*2-center] for x,y in XY]
    radius = [[] for i in range(SPLIT)]
    lim = [(100*i)**2 for i in range(1,SPLIT+1)]
    for i,(u,v,_) in enumerate(UVW):
        x,y = nXY[u]
        nx,ny = nXY[v]
        cx,cy = (x+nx)//2,(y+ny)//2

        rxy = cx**2+cy**2
        for j,li in enumerate(lim):
            if rxy <= li:
                radius[j].append(i)
                break
    
    pos_R = [-1]*m

    now = 0

    for i in range(SPLIT):
        rad = radius[i]
        random.shuffle(rad)

        for x in rad:
            pos_R[x] = now+1
            now = (now+1)%d
    return pos_R

def pos_split_R_clime():
    
    nXY = [[x*2-center,y*2-center] for x,y in XY]
    radius = [[] for i in range(SPLIT)]
    lim = [(100*i)**2 for i in range(1,SPLIT+1)]
    for i,(u,v,_) in enumerate(UVW):
        x,y = nXY[u]
        nx,ny = nXY[v]
        cx,cy = (x+nx)//2,(y+ny)//2

        rxy = cx**2+cy**2
        for j,li in enumerate(lim):
            if rxy <= li:
                radius[j].append((cx,cy,i))
                break
    
    pos_R = [-1]*m

    now = 0

    pos_X = [0]*d
    pos_Y = [0]*d
    num_d = [0]*d
    for i in range(SPLIT):
        rad = radius[i]
        random.shuffle(rad)

        for cx,cy,ind in rad:
            pos_R[ind] = now+1
            pos_X[now] += cx
            pos_Y[now] += cy
            num_d[now] += 1
            now = (now+1)%d

        # print(pos_X,pos_Y,num_d)
        upd = 0
        si = len(rad)
        while upd < si:
            a,b = random.randint(0,si-1),random.randint(0,si-1)
            ax,ay,aind = rad[a]
            bx,by,bind = rad[b]
            d1,d2 =  pos_R[aind]-1,pos_R[bind]-1
            if d1 == d2:
                continue
            
            dx,dy = ax-bx,ay-by
            base_size = (pos_X[d1]/num_d[d1])**2+(pos_Y[d1]/num_d[d1])**2+(pos_X[d2]/num_d[d2])**2+(pos_Y[d2]/num_d[d2])**2
            
            change_size = ((pos_X[d1]-dx)/num_d[d1])**2+((pos_Y[d1]-dy)/num_d[d1])**2+((pos_X[d2]+dx)/num_d[d2])**2+((pos_Y[d2]+dy)/num_d[d2])**2

            if base_size <= change_size:
                upd += 1
                continue

            upd = 0
            pos_X[d1] -= dx
            pos_Y[d1] -= dy
            pos_X[d2] += dx
            pos_Y[d2] += dy
            pos_R[aind],pos_R[bind] = pos_R[bind],pos_R[aind]

        # print(pos_X,pos_Y,num_d)
    return pos_R


class Master:

    def __init__(self):
        self.base_R = pos_split_R()
        self.DayInfos = []
        self._build()
        self.dist_score = 10**20
        self.upd_score = [0]*d
        self.score = [None]*d

    def _build(self):
        days_R = [[0]*m for i in range(d)]
        for i,r in enumerate(self.base_R):
            days_R[r-1][i] = 1

        for day_R in days_R:
            self.DayInfos.append(day_R)


    def calc_score(self,id):
        if self.upd_score[id]:
            return self.score[id]

        self.upd_score[id] = 1
        self.score[id] = dist_sum(self.DayInfos[id])
        return self.score[id]

    def dist_set(self,id,score):
        self.upd_score[id] = 1
        self.score[id] = score

    def out(self):
        print(*self.base_R)
        exit()


best_master = Master()
for i in range(d):
    print(f"day{i+1} dist={best_master.calc_score(i)}")
num1 = 0
num2 = 0

while time.time() - stime < TIME_LIM-0.5:
    num1 += 1
    e1,e2 = random.randint(0,m-1),random.randint(0,m-1)
    d1,d2 = best_master.base_R[e1]-1,best_master.base_R[e2]-1
    DayInfo1 = best_master.DayInfos[d1]
    DayInfo2 = best_master.DayInfos[d2]
    if d1 == d2:
        continue
    # if d1 == d2 or DayInfo1.spanning_tree[e2] or DayInfo2.spanning_tree[e1]:
    #     continue
    num2 += 1
    dist1 = best_master.calc_score(d1)
    dist2 = best_master.calc_score(d2)
    base_score = dist1 + dist2
    DayInfo1[e1],DayInfo1[e2] = 0,1
    DayInfo2[e1],DayInfo2[e2] = 1,0

    best_master.upd_score[d1] = 0
    best_master.upd_score[d2] = 0

    new_score = best_master.calc_score(d1) + best_master.calc_score(d2)

    if new_score > base_score:
        DayInfo1[e1],DayInfo1[e2] = 1,0
        DayInfo2[e1],DayInfo2[e2] = 0,1
        best_master.dist_set(d1,dist1)
        best_master.dist_set(d2,dist2)
    else:
        best_master.base_R[e1],best_master.base_R[e2] = d2+1,d1+1
print(num1,num2)
for i in range(d):
    print(f"day{i+1} dist={best_master.calc_score(i)}")
best_master.out()
