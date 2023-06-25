import time
import random
import copy
import sys
input = sys.stdin.readline
from heapq import heappush, heappop

stime = time.time()

TL = 1.9
DEBUG = 1

n = 30

le = n*(n+1)//2


class mincostflow:

    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

    def __init__(self, n):
        self.n = n
        self.pos = []
        self.g = [[] for i in range(n)]

    def add_edge(self, from_, to, cap, cost):
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_])-1, 0, -cost))
        return m

    def get_edge(self, i):
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        result = []
        for i in range(len(self.pos)):
            result.append(self.get_edge(i))
        return result

    def slope(self, s, t, flow_limit=10**20, inf=10**20):
        dual = [0]*self.n
        dist = [inf]*self.n
        pv = [-1]*self.n
        pe = [-1]*self.n
        vis = [False]*self.n

        def _dual_ref():
            nonlocal dual, dist, pv, pe, vis
            dist = [inf]*self.n
            pv = [-1]*self.n
            pe = [-1]*self.n
            vis = [False]*self.n

            que = [(0,s)]
            dist[s] = 0
            while que:
                _,v = heappop(que)
                if vis[v]:
                    continue
                vis[v] = True

                if v == t:
                    break
                for i in range(len(self.g[v])):
                    e = self.g[v][i]
                    if vis[e.to] or e.cap == 0:
                        continue
                    cost = e.cost - dual[e.to] + dual[v]
                    if dist[e.to] > dist[v] + cost:
                        dist[e.to] = dist[v] + cost
                        pv[e.to] = v
                        pe[e.to] = i
                        heappush(que, (dist[e.to],e.to))
            if not vis[t]:
                return False

            for v in range(self.n):
                if not vis[v]:
                    continue
                dual[v] -= dist[t] - dist[v]
            return True
        
        flow = 0
        cost = 0
        prev_cost = -1

        result = [(flow, cost)]
        while flow < flow_limit:
            if not _dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[pv[v]][pe[v]].cap)
                v = pv[v]

            v = t
            while v != s:
                e = self.g[pv[v]][pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = pv[v]
            
            d = -dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result

    def flow(self, s, t, flow_limit=10**20):
        return self.slope(s, t, flow_limit)[-1]
    

B = [list(map(int,input().split())) for i in range(30)]
pos_B = [[-1,-1] for i in range(le)]
par = [[[] for i in range(n)] for j in range(n)]
lis = [[] for i in range(n)]
for i in range(n):
    for j in range(i+1):
        b = B[i][j]
        pos_B[b] = [i,j]

pos_B_base = copy.deepcopy(pos_B)

target_X = [0]*le
num = 0
for i in range(n):
    for j in range(i+1):
        lis[i].append(num)
        target_X[num] = i
        num += 1

Dx = [-1,-1,0,0,1,1]
Dy = [-1,0,-1,1,0,1]


def around(x1,y1):

    pos = []
    for dx,dy in zip(Dx,Dy):
        nx,ny = x1+dx,y1+dy
        if nx < 0 or ny < 0:
            continue
        if ny <= nx:
            pos.append([nx,ny])
    
    return pos



def out(ans,score):
    print(len(ans))
    for a in ans:
        print(*a)


    if DEBUG:
        print(score)
    exit()

def calcScore(Base,ans):

    temp = copy.deepcopy(Base)

    err = 0
    for x1,y1,x2,y2 in ans:

        temp[x1][y1],temp[x2][y2] = temp[x2][y2],temp[x1][y1]

    
    for i in range(n-1):
        for j in range(i+1):
            if temp[i][j] > temp[i+1][j]:
                err += 1
            if temp[i][j] > temp[i+1][j+1]:
                err += 1
    

    if err:
        # print("err",err)
        return 50000 - 50*err

    
    ans_k = len(ans)

    # assert ans_k <= 10**4
    return 10**5 - 5*ans_k


temp_B = copy.deepcopy(B)
pos_B = copy.deepcopy(pos_B_base)

def swap(x1,y1,x2,y2,temp_B,pos_B):
    
    b1 = temp_B[x1][y1]
    b2 = temp_B[x2][y2]

    
    # print("swap",x1,y1,b1,x2,y2,b2)
    # assert [x2,y2] in around(x1,y1)

    temp_B[x1][y1],temp_B[x2][y2] = b2,b1
    pos_B[b1] = [x2,y2]
    pos_B[b2] = [x1,y1]



def dist2(x1,y1,x2,y2,temp_B,ret = 0):
    
    tx = target_X[temp_B[x1][y1]]


    dis = [[1000]*(i+1) for i in range(n)]
    dis[x1][y1] = 0

    h = [[0,x1,y1]]

    dif = x2-x1
    maxx = max(x1,x2)
    minx = min(x1,x2)
    while h:
        d,x,y = heappop(h)
        if dis[x][y] != d:
            continue

        for dx,dy in zip(Dx,Dy):
            if dif >= 0 and dx < 0 or dif <= 0 and dx > 0:
                continue
            nx,ny = x+dx,y+dy
            if nx < minx or nx > maxx or ny < 0 or ny > nx:
                continue

            if nx == x2 and dx == 0:
                continue
            # print(nx,ny)
            ntx = target_X[temp_B[nx][ny]]
            cost = d + 2


            if abs(ntx-x) > abs(ntx-nx):
                cost += 1
            
            if dis[nx][ny] == 1000:
                par[nx][ny] = []

            if dis[nx][ny] > cost:
                dis[nx][ny] = cost
                heappush(h,[cost,nx,ny])
                par[nx][ny] = [[x,y]]
            elif dis[nx][ny] == cost:
                par[nx][ny].append([x,y])

    

    # assert dis[x2][y2] < 1000

    if ret:
        paths = []
        tx,ty = x2,y2
        while (tx,ty) != (x1,y1):

            l = len(par[tx][ty])
            # rind = random.randint(0,l-1)
            rind = 0
            nx,ny = par[tx][ty][rind]

            paths.append([nx,ny,tx,ty])
            tx,ty = nx,ny

        return dis[x2][y2],paths[::-1]
    else:
        return dis[x2][y2]




def up(xi,yi,xj,yj,temp_ans,temp_B,pos_B):

    # assert xi > xj

    _,paths = dist2(xi,yi,xj,yj,temp_B,1)

    base = temp_B[xi][yi]
    for xi,yi,nxi,nyi in paths:
        swap(xi,yi,nxi,nyi,temp_B,pos_B)
        temp_ans.append([xi,yi,nxi,nyi])
        # print(xi,yi,nxi,nyi)
        # xi,yi = nxi,nyi
    # assert base == temp_B[xj][yj]


def down(xi,yi,xj,yj,temp_ans,temp_B,pos_B):
    # assert xi < xj

    _,paths = dist2(xi,yi,xj,yj,temp_B,1)

    for xi,yi,nxi,nyi in paths:
        swap(xi,yi,nxi,nyi,temp_B,pos_B)
        temp_ans.append([xi,yi,nxi,nyi])
        # print(xi,yi,nxi,nyi)
        xi,yi = nxi,nyi


def dist(x1,y1,x2,y2):
    if abs(x1-x2) >= abs(y1-y2):
        return (abs(x1-x2)+abs(y1-y2))//2
    else:
        return abs(y1-y2)




def calc3():
    
    temp_B = copy.deepcopy(B)
    pos_B = copy.deepcopy(pos_B_base)
    
    ### バブルソート的にやる
    temp_ans3 = []

    for loop in range(n):

        move_from = []
        move_to = []
        for i in lis[loop]:
            
            tx = target_X[i]
            xi,yi = pos_B[i]

            # assert xi >= tx,f"{i},{tx},{xi},{yi}"
            if xi <= tx:
                continue

            move_from.append([xi,yi,i])


        tx = loop

        for j in range(loop+1):
            nb = temp_B[tx][j]
            if target_X[nb] > tx:
                move_to.append([tx,j])

        # print(move_from,move_to)
        # assert len(move_from) == len(move_to)


        si = len(move_from)
        s = 2 * si

        t = s+1

        minflow = mincostflow(t+1)
        for i in range(si):
            minflow.add_edge(s,i,1,0)

        for i in range(si,si*2):
            minflow.add_edge(i,t,1,0)

        # paths = [[0]*si for i in range(si)]
        for i,(x1,y1,_) in enumerate(move_from):

            for j,(x2,y2) in enumerate(move_to):

                # d = dist(x1,y1,x2,y2)
                d = dist2(x1,y1,x2,y2,temp_B)
                # paths[i][j] = path

                minflow.add_edge(i,si+j,1,d)
            

        result = minflow.flow(s,t,si)
        # print(si,result)
        pars = []

        for e in minflow.edges():
            if e.from_ == s or e.to == t or e.flow == 0:
                continue

            f,t = e.from_,e.to-si
            x1,y1,ind = move_from[f]
            x2,y2 = move_to[t]

            pars.append([x1,y1,x2,y2,ind])
    
        pars.sort()
        # print(pars)
        for xi,yi,xj,yj,ind in pars:
            xi,yi = pos_B[ind]
            # assert target_X[temp_B[xi][yi]] == loop
            # assert pos_B[]
            up(xi,yi,xj,yj,temp_ans3,temp_B,pos_B)

        
    score = calcScore(B,temp_ans3)

    return temp_ans3,score



def calc4():
    
    temp_B = copy.deepcopy(B)
    pos_B = copy.deepcopy(pos_B_base)
    
    ### バブルソート的にやる
    temp_ans4 = []

    for loop in range(n//2):


        move_from = []
        move_to = []
        for i in lis[loop]:
            
            tx = target_X[i]
            xi,yi = pos_B[i]

            # assert xi >= tx,f"{i},{tx},{xi},{yi}"
            if xi <= tx:
                continue

            move_from.append([xi,yi,i])


        tx = loop

        for j in range(loop+1):
            nb = temp_B[tx][j]
            if target_X[nb] > tx:
                move_to.append([tx,j])

        # print(move_from,move_to)
        # assert len(move_from) == len(move_to)


        si = len(move_from)
        s = 2 * si

        t = s+1

        minflow = mincostflow(t+1)
        for i in range(si):
            minflow.add_edge(s,i,1,0)

        for i in range(si,si*2):
            minflow.add_edge(i,t,1,0)


        # paths = [[0]*si for i in range(si)]
        for i,(x1,y1,_) in enumerate(move_from):

            for j,(x2,y2) in enumerate(move_to):

                # d = dist(x1,y1,x2,y2)
                d = dist2(x1,y1,x2,y2,temp_B)
                # paths[i][j] = path
                minflow.add_edge(i,si+j,1,d)
            

        result = minflow.flow(s,t,si)
        # print(si,result)
        pars = []

        for e in minflow.edges():
            if e.from_ == s or e.to == t or e.flow == 0:
                continue

            f,t = e.from_,e.to-si
            x1,y1,ind = move_from[f]
            x2,y2 = move_to[t]

            pars.append([x1,y1,x2,y2,ind])
    
        pars.sort()
        # print(pars)
        for xi,yi,xj,yj,ind in pars:
            
            xi,yi = pos_B[ind]
            # assert target_X[temp_B[xi][yi]] == loop
            # assert pos_B[]
            up(xi,yi,xj,yj,temp_ans4,temp_B,pos_B)



        move_from = []
        move_to = []
        for i in lis[-1-loop]:
            
            tx = target_X[i]
            xi,yi = pos_B[i]

            # assert xi <= tx,f"{i},{tx},{xi},{yi}"
            if xi >= tx:
                continue

            move_from.append([xi,yi,i])


        tx = n-1-loop

        for j in range(tx+1):
            nb = temp_B[tx][j]
            if target_X[nb] < tx:
                move_to.append([tx,j])

        # print(move_from,move_to)
        # assert len(move_from) == len(move_to)


        si = len(move_from)
        s = 2 * si

        t = s+1

        minflow = mincostflow(t+1)
        for i in range(si):
            minflow.add_edge(s,i,1,0)

        for i in range(si,si*2):
            minflow.add_edge(i,t,1,0)


        # paths = [[0]*si for i in range(si)]
        for i,(x1,y1,_) in enumerate(move_from):

            for j,(x2,y2) in enumerate(move_to):

                # d = dist(x1,y1,x2,y2)
                d = dist2(x1,y1,x2,y2,temp_B)
                # paths[i][j] = path
                minflow.add_edge(i,si+j,1,d)
            

        result = minflow.flow(s,t,si)
        # print(si,result)
        pars = []

        for e in minflow.edges():
            if e.from_ == s or e.to == t or e.flow == 0:
                continue

            f,t = e.from_,e.to-si
            x1,y1,ind = move_from[f]
            x2,y2 = move_to[t]

            pars.append([x1,y1,x2,y2,ind])
    
        pars.sort(reverse=True)
        # print(pars)
        for xi,yi,xj,yj,ind in pars:
            xi,yi = pos_B[ind]
            # assert target_X[temp_B[xi][yi]] == tx
            # assert pos_B[]
            down(xi,yi,xj,yj,temp_ans4,temp_B,pos_B)

        
    score = calcScore(B,temp_ans4)

    return temp_ans4,score


temp_ans3,score3 = calc3()

temp_ans,score = calc4()

if score3 > score:
    score = score3
    temp_ans = temp_ans3



out(temp_ans,score)
