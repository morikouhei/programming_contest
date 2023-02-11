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
# cen = [inf,-1]

for i,(x,y) in enumerate(XY):
    if xma[0] < x:
        xma = [x,i]
    if xmi[0] > x:
        xmi = [x,i]
    
    if yma[0] < y:
        yma = [y,i]
    if ymi[0] > y:
        ymi = [y,i]
    
    # r = (x-500)**2+(y-500)**2
    # if cen[0] > r:
    #     cen = [r,i]

dist_point = set([xma[1],xmi[1],yma[1],ymi[1]])

# dist_point = set([xma[1],xmi[1],yma[1],ymi[1],cen[1]])
# dist_lis = [inf]*m
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

class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]


def make_base_R():
    base_R = []
    for i in range(1,d+1):
        need = m//d
        if m%d >= i:
            need += 1
        for j in range(need):
            base_R.append(i)
    return base_R

def pos_split_R():


    nXY = [[x*2-center,y*2-center] for x,y in XY]
    radius = [[] for i in range(SPLIT)]
    lim = [(100*i)**2 for i in range(1,SPLIT+1)]
    for i,(u,v,_) in enumerate(UVW):
        x,y = nXY[u]
        nx,ny = nXY[v]
        cx,cy = (x+nx)//2,(y+ny)//2

        rxy = cx**2+cy**2
        if i < 10:
            print(u,v,cx,cy,rxy)
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
        if i < 10:
            print(u,v,cx,cy,rxy)
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
        print(len(rad))
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


def out(R):
    print(*R)
    exit()

class DayInfo:

    def __init__(self,road):
        self.road = road
        self.uf = Unionfind(n)
        self.tree_created = False
        self.spanning_tree = [0]*m
        self.inf_path_num = 0
        self.upd = False
        self.dist_sum = inf
        self._build()



    def _build(self):
        road_info = [[x,i] for i,x in enumerate(self.road)]
        random.shuffle(road_info)
        for use,ind in road_info:
            if use:
                continue
            u,v,_ = UVW[ind]
            if self.uf.same(u,v):
                continue
            self.uf.union(u,v)
            self.spanning_tree[ind] = 1
        
        if self.uf.size(0) == n:
            self.tree_created = True

        else:
            for i in range(n):
                if self.uf.find(i) == i:
                    si = self.uf.size(i)
                    self.inf_path_num += si*(n-si)
    
    def rebuild(self,ind=None):

        self.spanning_tree = [0]*m
        self.uf = Unionfind(n)
        self.tree_created = False
        road_info = [[x,i] for i,x in enumerate(self.road)]
        random.shuffle(road_info)
        if ind != None:
            for i in range(m):
                if road_info[i][1] == ind:
                    road_info = road_info[:i] + road_info[i+1:] + [road_info[i]]
                    break

        for use,ind in road_info:
            if use:
                continue
            u,v,_ = UVW[ind]
            if self.uf.same(u,v):
                continue
            self.uf.union(u,v)
            self.spanning_tree[ind] = 1
        
        if self.uf.size(0) == n:
            self.tree_created = True

        else:
            self.inf_path_num = 0
            for i in range(n):
                if self.uf.find(i) == i:
                    si = self.uf.size(i)
                    self.inf_path_num += si*(n-si)

    def calc_dist(self):
        if self.upd:
            return self.dist_sum
        self.dist_sum = dist_sum(self.road)
        self.upd = True
        return self.dist_sum

    def dist_set(self,dist):
        assert self.upd
        self.dist_sum = dist


class Master:

    def __init__(self):
        # self.base_R = make_base_R()
        # random.shuffle(self.base_R)
        self.base_R = pos_split_R_clime()
        self.DayInfos = []
        self.has_load = [set() for i in range(d)]
        self._build()
        self.dist_score = 10**20
        self.upd_score = False

    def _build(self):
        days_R = [[0]*m for i in range(d)]
        for i,r in enumerate(self.base_R):
            days_R[r-1][i] = 1
            self.has_load[r-1].add(i)

        for day_R in days_R:
            self.DayInfos.append(DayInfo(day_R))

    
    def check_tree(self):
        for dayInfo in self.DayInfos:
            if dayInfo.tree_created == False:
                return False
        return True

    def check_inf_num(self):
        inf_num = 0
        for dayInfo in self.DayInfos:
            inf_num += dayInfo.inf_path_num
        return inf_num

    def make_tree(self):
        if self.check_tree():
            return True

        for i,r in enumerate(self.base_R):
            u,v,_ = UVW[i]

            ### if already same group, continue
            if self.DayInfos[r-1].uf.same(u,v):
                continue

            ### if group is different, try to swap with other dayinfo

            s = random.randint(0,d-1)
            for j in range(d):
                ss = (j+s)%d
                if ss == r-1:
                    continue
                if self.DayInfos[ss].spanning_tree[i]:
                    continue
                
                find_edge = -1
                for edge in self.has_load[ss]:
                    if self.DayInfos[r-1].spanning_tree[edge]:
                        continue
                    find_edge = edge
                    break

                if find_edge == -1:
                    continue

                self.base_R[edge],self.base_R[i] = r,ss+1
                
                self.DayInfos[r-1].spanning_tree[i] = 1
                self.has_load[r-1].remove(i)
                self.has_load[r-1].add(edge)
                self.has_load[ss].remove(edge)
                self.has_load[ss].add(i)
                self.DayInfos[r-1].road[edge],self.DayInfos[r-1].road[i] = 1,0
                self.DayInfos[ss].road[edge],self.DayInfos[ss].road[i] = 0,1
                break
        self.upd_score = False

        if self.check_tree():
            return True
        else:
            return False

    def make_tree_hard(self):
        if self.check_tree():
            return True

        for i,r in enumerate(self.base_R):
            u,v,_ = UVW[i]

            ### if already same group, continue
            if self.DayInfos[r-1].uf.same(u,v):
                continue

            ### if group is different, try to swap with other dayinfo

            s = random.randint(0,d-1)
            for j in range(d):
                ss = (j+s)%d
                if ss == r-1:
                    continue
                if self.DayInfos[ss].spanning_tree[i]:
                    self.DayInfos[ss].rebuild(i)
                
                if self.DayInfos[ss].spanning_tree[i]:
                    continue

                find_edge = -1
                for edge in self.has_load[ss]:
                    if self.DayInfos[r-1].spanning_tree[edge]:
                        continue
                    find_edge = edge
                    break

                if find_edge == -1:
                    continue

                self.base_R[edge],self.base_R[i] = r,ss+1
                
                self.DayInfos[r-1].spanning_tree[i] = 1
                self.has_load[r-1].remove(i)
                self.has_load[r-1].add(edge)
                self.has_load[ss].remove(edge)
                self.has_load[ss].add(i)
                self.DayInfos[r-1].road[edge],self.DayInfos[r-1].road[i] = 1,0
                self.DayInfos[ss].road[edge],self.DayInfos[ss].road[i] = 0,1
                break
        self.upd_score = False

        if self.check_tree():
            return True
        else:
            return False


    def calc_score(self):
        if self.upd_score:
            return self.dist_score

        self.dist_score = 0
        for dayInfo in self.DayInfos:
            self.dist_score += dayInfo.calc_dist()
        
        self.upd_score = True
        return self.dist_score


    def out(self):
        print(*self.base_R)
        exit()


best_master = Master()
# best_score = best_master.calc_score()
# tree_made = best_master.check_tree()
# inf_num = best_master.check_inf_num()

# TREE_LIM = 0.8
# while time.time() - stime < TREE_LIM:
#     master = Master()
#     made = master.make_tree()
#     # if made == False:
#     #     made = master.make_tree_hard()

#     now_score = master.calc_score()
#     now_inf_num = master.check_inf_num()
#     if tree_made == False and master.check_tree():
#         best_score = now_score
#         best_master = master
#         tree_made = master.check_tree()
#         inf_num = now_inf_num
#         continue

#     if now_inf_num < inf_num:
#         best_score = now_score
#         best_master = master
#         tree_made = master.check_tree()
#         inf_num = now_inf_num
#     elif now_inf_num == inf_num:
#         if now_score < best_score:
#             if tree_made and master.check_tree() == False:
#                 continue
#             best_score = now_score
#             best_master = master
#             tree_made = master.check_tree()

# print(*best_master.base_R)
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
    dist1 = DayInfo1.calc_dist()
    dist2 = DayInfo2.calc_dist()
    base_score = dist1 + dist2
    DayInfo1.road[e1],DayInfo1.road[e2] = 0,1
    DayInfo2.road[e1],DayInfo2.road[e2] = 1,0

    DayInfo1.upd = False
    DayInfo2.upd = False
    new_score = DayInfo1.calc_dist()+DayInfo2.calc_dist()

    if new_score > base_score:
        DayInfo1.road[e1],DayInfo1.road[e2] = 1,0
        DayInfo2.road[e1],DayInfo2.road[e2] = 0,1
        DayInfo1.dist_set(dist1)
        DayInfo2.dist_set(dist2)
    else:
        best_master.base_R[e1],best_master.base_R[e2] = d2+1,d1+1
print(num1,num2)
best_master.out()
