import random
import heapq
import time
import sys
from enum import Enum
from collections import deque

STIME = time.time()
TIME_LIM = 5
inf = 10**10

N,W,K,C = map(int,input().split())
N2 = N**2
AB = [list(map(int,input().split())) for i in range(W)]
CD = [list(map(int,input().split())) for i in range(K)]

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

def toId(x,y):
    return x*N+y

def toPos(id):
    return divmod(id,N)

class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1

DXY = [[1,0],[0,1],[-1,0],[0,-1]]

Xmin,Xmax = N+1,-1
Ymin,Ymax = N+1,-1

for x,y in AB+CD:
    Xmin = min(Xmin,x)
    Xmax = max(Xmax,x)
    Ymin = min(Ymin,y)
    Ymax = max(Ymax,y)



### Phase 1, Make Grid and point_list
GRID_NUM = 70

GRID_SIZE = [10,20]
GRID_LINE = [[0]*N for i in range(N)]
best_num = -1
best_size = []
for gx in range(GRID_SIZE[0],GRID_SIZE[1]+1):
    for gy in range(GRID_SIZE[0],GRID_SIZE[1]+1):
        nx = (Xmax-Xmin+gx-1)//gx + 1
        ny = (Ymax-Ymin+gy-1)//gy + 1
        nxy = nx*ny
        if nxy < GRID_NUM:
            if best_num >= GRID_NUM:
                continue
            if best_num < nxy:
                best_num = nxy
                best_size = [gx,gy]
        else:
            if best_num < GRID_NUM:
                best_num = nxy
                best_size = [gx,gy]
            else:
                if best_num > GRID_NUM:
                    best_num = nxy
                    best_size = [gx,gy]


X_BOTTOM = Xmin
Y_BOTTOM = Ymin
GX,GY = best_size
nx = (Xmax-Xmin+GX-1)//GX + 1
ny = (Ymax-Ymin+GY-1)//GY + 1
X_TOP = X_BOTTOM + (nx-1)*GX
Y_TOP = Y_BOTTOM + (ny-1)*GY

def adjust_pos(bottom,top,dx,nx):
    if top < N:
        X_list = [bottom+dx*i for i in range(nx)]
    else:
        over = top - (N - 1)
        dGX = [dx]*(nx-1)
        now = 0
        while over:
            over -= 1
            dGX[now] -= 1
            now = (now+1)%(nx-1)
        X_list = [bottom]
        for dgx in dGX:
            X_list.append(X_list[-1]+dgx)

    assert X_list[-1] < N
    return X_list

X_list = adjust_pos(X_BOTTOM,X_TOP,GX,nx)

Y_list = adjust_pos(Y_BOTTOM,Y_TOP,GY,ny)

X_TOP = X_list[-1]
Y_TOP = Y_list[-1]

print("#", X_BOTTOM,X_TOP,Y_BOTTOM,Y_TOP,GX,GY,best_num)

for x in X_list:
    for y in range(Y_BOTTOM,Y_TOP+1):
        GRID_LINE[x][y] = 1

for y in Y_list:
    for x in range(X_BOTTOM,X_TOP+1):
        GRID_LINE[x][y] = 1


Is_Broken = [[0]*N for i in range(N)]
power_estimate = [[-1]*N for i in range(N)]
power_used = [[0]*N for i in range(N)]


### TODO update parameter
def get_power(x,y):
    if power_used[x][y] == 0:
        return 50

    if C >= 32:
        return 100
    else:
        return 50



def query(x: int, y: int, power: int):
    print(f"{x} {y} {power}", flush=True)
    res = Response(int(input()))
    if res in (Response.BROKEN, Response.FINISH):
        Is_Broken[x][y] = 1
    return res

def destruct_naive(x,y,flg = 0):
    # excavate (y, x) with fixed power until destruction
    power = get_power(x,y)
    if flg:
        lim = 5000
    else:
        lim = 1000

    first = 1
    while not Is_Broken[x][y] and power_used[x][y] < lim:
        if first:
            print("# estimation of ",x,y,power_estimate[x][y])
        result = query(x,y, power)
        power_used[x][y] += power
        if result == Response.FINISH:
            # print(f"total_cost={self.total_cost}", file=sys.stderr)
            sys.exit(0)
        elif result == Response.INVALID:
            print(f"invalid: x={x} y={y}", file=sys.stderr)
            sys.exit(1)
    
    if Is_Broken[x][y]:
        power_estimate[x][y] = power_used[x][y]


def destruct_predict(x,y):

    if Is_Broken[x][y]:
        return

    p_estimate = power_estimate[x][y]

    left_estimate = p_estimate - power_used[x][y]

    first_power = left_estimate - random.randint(50,100)
    first_power = max(first_power,get_power(x,y))

    result = query(x,y, first_power)
    power_used[x][y] += first_power
    if result == Response.FINISH:
        # print(f"total_cost={self.total_cost}", file=sys.stderr)
        sys.exit(0)
    elif result == Response.INVALID:
        print(f"invalid: x={x} y={y}", file=sys.stderr)
        sys.exit(1)

    while not Is_Broken[x][y]:
        power = get_power(x,y)
        result = query(x,y, power)
        power_used[x][y] += power
        if result == Response.FINISH:
            # print(f"total_cost={self.total_cost}", file=sys.stderr)
            sys.exit(0)
        elif result == Response.INVALID:
            print(f"invalid: x={x} y={y}", file=sys.stderr)
            sys.exit(1)

    if Is_Broken[x][y]:
        power_estimate[x][y] = power_used[x][y]


def destruct_once(x,y,power):
    # excavate (y, x) with fixed power until destruction
    if Is_Broken[x][y]:
        return 
    result = query(x,y, power)
    power_used[x][y] += power
    if result == Response.FINISH:
        # print(f"total_cost={self.total_cost}", file=sys.stderr)
        sys.exit(0)
    elif result == Response.INVALID:
        print(f"invalid: x={x} y={y}", file=sys.stderr)
        sys.exit(1)
    
    if Is_Broken[x][y]:
        power_estimate[x][y] = power_used[x][y]


class Solver:
    def __init__(self):
        self.Cross_Point = [[-1]*N for i in range(N)]
        self.point_id = 0
        self.point_list = []
        self.dist = []
        self.vis = []
        self.par = []
        self.vis_id = 0
        self.edge_used = []
        self.e = [[]]
        self.edge_num = 0
        self.uf = []
        self.finish_estimate = set()
        self.edge_list = []
        self.is_source = []
        self.point_used = []
        self.root_list = [[] for i in range(K)]
        self.best_score = inf
        self.best_edge_used = []
        self.search_vis = []

    def point_add(self,x,y,id):
        if self.Cross_Point[x][y] != -1:
            return

        self.Cross_Point[x][y] = self.point_id
        self.point_id += 1
        self.point_list.append([x,y,id])



    def build_graph(self):
        size = self.point_id
        self.e = [[] for i in range(size)]
        self.vis = [0]*size
        self.par = [0]*size
        self.dist = [inf]*size
        self.uf = Unionfind(size)
        self.is_source = [0]*size
        self.point_used = [0]*size
        self.search_vis = [0]*size

        for i in range(N):
            
            if i not in X_list:
                continue

            lid = -1
            for j in range(N):
                nid = self.Cross_Point[i][j]
                if nid == -1:
                    continue

                if lid == -1:
                    lid = nid
                    continue

                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1
                lid = nid

        
        for i in range(N):
            if i not in Y_list:
                continue
            lid = -1
            for j in range(N):
                nid = self.Cross_Point[j][i]
                if nid == -1:
                    continue

                if lid == -1:
                    lid = nid
                    continue
                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1
                lid = nid

        
        for x in range(N):
            for y in range(N):
                if self.Cross_Point[x][y] == -1:
                    continue
                if GRID_LINE[x][y]:
                    continue
            
                lid = self.Cross_Point[x][y]
                lx = -1
                rx = -1
                for i in range(len(X_list)-1):
                    if X_list[i] < x:
                        lx = X_list[i]
                        rx = X_list[i+1]
                nid = self.Cross_Point[lx][y]
                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1

                nid = self.Cross_Point[rx][y]
                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1

                ly = -1
                ry = -1
                for i in range(len(Y_list)-1):
                    if Y_list[i] < y:
                        ly = Y_list[i]
                        ry = Y_list[i+1]

                nid = self.Cross_Point[x][ly]
                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1

                nid = self.Cross_Point[x][ry]
                self.e[lid].append([nid,inf,self.edge_num])
                self.e[nid].append([lid,inf,self.edge_num])
                self.edge_list.append([nid,lid,inf])
                self.edge_num += 1


        self.edge_used = [0]*self.edge_num

        for a,b in AB:
            self.is_source[self.Cross_Point[a][b]] = 1

    def destruct_line(self,id,nid):
        x,y,_ = self.point_list[id]
        nx,ny,_ = self.point_list[nid]
        dx,dy = 0,0
        if x < nx:
            dx = 1
        if x > nx:
            dx = -1

        if y < ny:
            dy = 1
        if y > ny:
            dy = -1

        
        while x != nx or y != ny:
            destruct_naive(x,y,1)
            x,y = x+dx,y+dy
            
        destruct_naive(x,y,1)

    def destruct_test(self):
        for i in range(self.point_id):
            for nid,_,_ in self.e[i]:
                self.destruct_line(i,nid)


    def estimate_line(self,id,nid):
        if (id,nid) in self.finish_estimate or (nid,id) in self.finish_estimate:
            return
        
        self.finish_estimate.add((id,nid))
        self.finish_estimate.add((nid,id))

        x,y,_ = self.point_list[id]
        nx,ny,_ = self.point_list[nid]

        p1 = power_estimate[x][y]
        p2 = power_estimate[nx][ny]

        dx,dy = 0,0
        if x < nx:
            dx = 1
        if x > nx:
            dx = -1

        if y < ny:
            dy = 1
        if y > ny:
            dy = -1

    
        dist = abs(x-nx)+abs(y-ny)
        dp = abs(p2-p1)//dist
        if p2 - p1 < 0:
            dp = -dp
        p_now = p1

        while x != nx or y != ny:
            x,y = x+dx,y+dy
            p_now += dp
            power_estimate[x][y] = p_now
            assert p_now >= 0
            

    def get_estimate_power(self,id,nid):
        x,y,_ = self.point_list[id]
        nx,ny,_ = self.point_list[nid]

        p1 = power_estimate[x][y]
        p2 = power_estimate[nx][ny]

        dx,dy = 0,0
        if x < nx:
            dx = 1
        if x > nx:
            dx = -1

        if y < ny:
            dy = 1
        if y > ny:
            dy = -1

    
        power_sum = 0

        while x != nx or y != ny:
            x,y = x+dx,y+dy
            power_sum += power_estimate[x][y]

        return power_sum

    def graph_connected(self):

        for c,d in CD:
            ok = 0
            id = self.Cross_Point[c][d]
            for a,b in AB:
                nid = self.Cross_Point[a][b]
                if self.uf.same(id,nid):
                    ok = 1
            if ok == 0:
                return 0

        return 1



    def get_root(self,id):
        x,y = CD[id]
        sid = self.Cross_Point[x][y]
        vis_id = self.vis_id
        self.dist[sid] = 0
        self.vis[sid] = vis_id

        root = []
        h = [[0,sid]]
        best_dis = inf
        best_id = -1
        while h:
            d,now = heapq.heappop(h)
            if self.dist[now] != d:
                continue

            for nex,nd,edge_id in self.e[now]:
                if self.vis[nex] == vis_id and self.dist[nex] <= d+nd:
                    continue
                self.dist[nex] = d+nd
                self.par[nex] = [now,edge_id]
                self.vis[nex] = vis_id
                if self.point_used[nex] or self.is_source[nex]:
                    if best_dis > self.dist[nex]:
                        best_dis = self.dist[nex]
                        best_id = nex
                    continue

                heapq.heappush(h,[d+nd,nex])

        assert best_id != -1
        self.vis_id += 1
        now = best_id
        while now != sid:
            nex,edge_id = self.par[now]
            root.append([now,edge_id])
            now = nex
        root.append([sid,-1])
        root = root[::-1]
        
        if self.is_source[best_id]:
            return root

        for i in range(K):
            if not self.point_used[best_id] >> i & 1:
                continue

            find = 0
            for r in self.root_list[i]:

                if find:
                    root.append(r)

                if r[0] == best_id:
                    find = 1

        return root

    def estimate_line_update(self,x,y,nx,ny):

        p1 = power_estimate[x][y]
        p2 = power_estimate[nx][ny]

        dx,dy = 0,0
        if x < nx:
            dx = 1
        if x > nx:
            dx = -1

        if y < ny:
            dy = 1
        if y > ny:
            dy = -1

    
        dist = abs(x-nx)+abs(y-ny)

        dp = abs(p2-p1)//dist
        if p2 - p1 < 0:
            dp = -dp
        p_now = p1
        # print("#",p1,p2,dist,dp,x,y,nx,ny)
        while x != nx or y != ny:
            x,y = x+dx,y+dy
            p_now += dp
            power_estimate[x][y] = p_now
            assert p_now >= 0
    def destruct_line_estimate(self,id,nid):
        x,y,_ = self.point_list[id]
        nx,ny,_ = self.point_list[nid]
        dx,dy = 0,0
        if x < nx:
            dx = 1
        if x > nx:
            dx = -1

        if y < ny:
            dy = 1
        if y > ny:
            dy = -1

        
        while x != nx or y != ny:
            destruct_predict(x,y)
            self.estimate_line_update(x,y,nx,ny)
            x,y = x+dx,y+dy

            
        destruct_predict(x,y)

    def neighbor_update(self):

        for x,y in CD:
            if GRID_LINE[x][y]:
                continue
        
            lid = self.Cross_Point[x][y]
            power_lid = power_estimate[x][y]
            lx = -1
            rx = -1
            for i in range(len(X_list)-1):
                if X_list[i] < x:
                    lx = X_list[i]
                    rx = X_list[i+1]

            nid = self.Cross_Point[lx][y]
            power_estimate[lx][y] = power_lid
            self.estimate_line(lid,nid)

            nid = self.Cross_Point[rx][y]
            power_estimate[rx][y] = power_lid
            self.estimate_line(lid,nid)

            ly = -1
            ry = -1
            for i in range(len(Y_list)-1):
                if Y_list[i] < y:
                    ly = Y_list[i]
                    ry = Y_list[i+1]

            nid = self.Cross_Point[x][ly]
            power_estimate[x][ly] = power_lid
            self.estimate_line(lid,nid)

            nid = self.Cross_Point[x][ry]
            power_estimate[x][ry] = power_lid
            self.estimate_line(lid,nid)

    def calc_score(self,edge_used_list):
        count = 0
        for i,use in enumerate(edge_used_list):
            if use:
                count += self.edge_list[i][2]

        return count

    def climbing(self):
        for i in range(K):
            root = self.get_root(i)
            id = 1<<i
      
            for index,edge_index in root:
                self.point_used[index] |= id
                if edge_index != -1:
                    self.edge_used[edge_index] |= id

        
        self.best_score = self.calc_score(self.edge_used)
        self.best_edge_used = self.edge_used[:]
        print("#",self.best_score)
        while time.time() - STIME < 3:
            self.edge_used = [0]*self.edge_num
            self.point_used = [0]*self.point_id
            Kid = list(range(K))
            random.shuffle(Kid)
            for i in Kid:
                root = self.get_root(i)
                id = 1<<i
                for index,edge_index in root:
                    self.point_used[index] |= id
                    if edge_index != -1:
                        self.edge_used[edge_index] |= id

            
            now_score = self.calc_score(self.edge_used)

            if now_score < self.best_score:
                print("#",now_score,self.best_score,time.time()-STIME)
                self.best_score = now_score
                self.best_edge_used = self.edge_used[:]

    def graph_search(self,q:deque,power_lim):

        nq = deque([])

        while q:
            now = q.pop()
            x,y,_ = self.point_list[now]


            while power_estimate[x][y] == -1 and power_used[x][y] < power_lim:
                destruct_once(x,y,get_power(x,y))
            
            if power_estimate[x][y] == -1:
                nq.append(now)
                continue

            if self.is_source[now]:
                continue

            for nex,_,_ in self.e[now]:
                if self.search_vis[nex] == power_lim:
                    continue
                self.search_vis[nex] = power_lim
                q.append(nex)

        return nq


    def update_graph(self):


        # q = deque([])
        # for c,d in CD:
        #     q.append(self.Cross_Point[c][d])
        #     self.search_vis[self.Cross_Point[c][d]] = 1
        # self.neighbor_update()

        for que in range(1,5000):
            power_lim = que*get_power(0,0)

            q = deque([])
            for c,d in CD:
                id = self.Cross_Point[c][d]
                find = 0
                for a,b in AB:
                    if self.uf.same(id,self.Cross_Point[a][b]):
                        find = 1
                
                if find:
                    continue
                q.append(id)
                self.search_vis[id] = power_lim

            q = self.graph_search(q,power_lim)
            ## query once
            # for x in X_list:
            #     for y in Y_list:
            #         destruct_once(x,y,get_power(x,y))

            
            # for x,y in AB:
            #     destruct_once(x,y,get_power(x,y))

            ### update estimation of graph
            for x in X_list:
                for i in range(len(Y_list)-1):
                    y = Y_list[i]
                    ny = Y_list[i+1]
                    id = self.Cross_Point[x][y]
                    if power_estimate[x][y] == -1:
                        continue

                    if ny <= Y_TOP and power_estimate[x][ny] != -1:
                        self.estimate_line(id,self.Cross_Point[x][ny])

            for y in Y_list:
                for i in range(len(X_list)-1):
                    x = X_list[i]
                    nx = X_list[i+1]
                    id = self.Cross_Point[x][y]
                    if power_estimate[x][y] == -1:
                        continue
                    if nx <= X_TOP and power_estimate[nx][y] != -1:
                        self.estimate_line(id,self.Cross_Point[nx][y])

            for i in range(self.point_id):
                x,y,_ = self.point_list[i]
                if power_estimate[x][y] == -1:
                    continue

                for j in range(len(self.e[i])):
                    nid,d,eid = self.e[i][j]
                    if d != inf:
                        continue
                    nx,ny,_ = self.point_list[nid]
                    if power_estimate[nx][ny] == -1:
                        continue
                    self.estimate_line(i,nid)
                    self.uf.union(i,nid)

                    power_sum = self.get_estimate_power(i,nid)
                    self.e[i][j][1] = power_sum
                    self.edge_list[eid][2] = power_sum

            
            if self.graph_connected() == 0:
                continue
            
            print("# query = ",que)


            self.climbing()

            for edge_used,(id,nid,_) in zip(self.best_edge_used,self.edge_list):
                if edge_used == 0:
                    continue
                self.destruct_line_estimate(id,nid)
                # self.destruct_line(id,nid)

            assert False

        




# Cross_point = [[-1]*N for i in range(N)]

# point_list = []
# point_num = 0

# def point_add(x,y):
#     global point_num
#     Cross_point[x][y] = point_num
#     point_num += 1
#     print("#",x,y)
#     point_list.append([x,y])



solver = Solver()
for x,y in CD:
    if solver.Cross_Point[x][y] != -1:
        continue

    solver.point_add(x,y,1)
    destruct_naive(x,y,1)
    ### in the line of grid 
    if GRID_LINE[x][y]:
        continue
    lx = -1
    rx = -1
    for i in range(len(X_list)-1):
        if X_list[i] < x:
            lx = X_list[i]
            rx = X_list[i+1]

    solver.point_add(lx,y,2)
    solver.point_add(rx,y,2)

    ly = -1
    ry = -1
    for i in range(len(Y_list)-1):
        if Y_list[i] < y:
            ly = Y_list[i]
            ry = Y_list[i+1]
    solver.point_add(x,ly,2)
    solver.point_add(x,ry,2)

for x,y in AB:
    if solver.Cross_Point[x][y] != -1:
        continue

    solver.point_add(x,y,1)
    # destruct_naive(x,y)
    ### in the line of grid 
    if GRID_LINE[x][y]:
        continue
    lx = -1
    rx = -1
    for i in range(len(X_list)-1):
        if X_list[i] < x:
            lx = X_list[i]
            rx = X_list[i+1]

    solver.point_add(lx,y,2)
    solver.point_add(rx,y,2)

    ly = -1
    ry = -1
    for i in range(len(Y_list)-1):
        if Y_list[i] < y:
            ly = Y_list[i]
            ry = Y_list[i+1]
    solver.point_add(x,ly,2)
    solver.point_add(x,ry,2)


for x in X_list:
    for y in Y_list:
        solver.point_add(x,y,0)
        # destruct_once(x,y,get_power(x,y))




solver.build_graph()
solver.update_graph()