from heapq import heappush,heappop
from collections import deque
import time
import random

TIME_LIM = 2
stime = time.time()




T,H,W,i0 = map(int,input().split())
SX,SY = i0,0
inf = 1<<10
lim = 0
def gen_walls(rng, H, W, h, v, distance_lb=1):

    def abs_diff(a, b):
        return abs(a - b)

    def sample(rng, num_tie):
        return random.randint(0, num_tie - 1)

    def bernoulli(rng, p):
        return random.random() < p


    adj = [[[] for _ in range(W + 1)] for _ in range(H + 1)]

    for i in range(H + 1):
        for j in range(W + 1):
            if i > 0:
                adj[i - 1][j].append((i, j))
                adj[i][j].append((i - 1, j))
            if j > 0:
                adj[i][j - 1].append((i, j))
                adj[i][j].append((i, j - 1))

    marked = [[False] * (W + 1) for _ in range(H + 1)]

    for i in range(H + 1):
        marked[i][0] = True
        marked[i][W] = True
    for j in range(W + 1):
        marked[0][j] = True
        marked[H][j] = True


    for i in range(H-1):
        for j in range(W):
            if h[i][j] == 0:
                continue
            marked[i+1][j] = True
            marked[i+1][j+1] = True
    
    for i in range(H):
        for j in range(W-1):
            if v[i][j] == 0:
                continue
            marked[i][j+1] = True
            marked[i+1][j+1] = True

    while True:
        candidates = []
        q = []
        dist = [[-1] * (W + 1) for _ in range(H + 1)]

        for i in range(H + 1):
            for j in range(W + 1):
                if marked[i][j]:
                    q.append((i, j))
                    dist[i][j] = 0

        while q:
            i, j = q.pop(0)
            dij = dist[i][j]
            for i1, j1 in adj[i][j]:
                if dist[i1][j1] == -1:
                    dist[i1][j1] = dij + 1
                    if dij + 1 > distance_lb:
                        candidates.append((i1, j1))
                    q.append((i1, j1))

        if not candidates:
            break

        i, j = random.choice(candidates)
        ti, tj = 0, 0
        d = i + j
        num_tie = 0

        for i1 in range(H + 1):
            for j1 in range(W + 1):
                if dist[i1][j1] == 0:
                    d1 = abs_diff(i, i1) + abs_diff(j, j1)
                    if d > d1:
                        ti = i1
                        tj = j1
                        d = d1
                        num_tie = 1
                    elif d == d1:
                        num_tie += 1
                        if sample(rng, num_tie) == 0:
                            ti = i1
                            tj = j1

        assert abs_diff(i, ti) + abs_diff(j, tj) > distance_lb

        assert j > 0
        assert i > 0
        assert ti > 0 or j == tj
        assert tj > 0 or i == ti

        if bernoulli(rng, 0.5):
            if i < ti:
                for i1 in range(i, ti):
                    v[i1][j - 1] = 1
                    marked[i1][j] = True
            else:
                for i1 in range(ti + 1, i + 1):
                    v[i1 - 1][j - 1] = 1
                    marked[i1][j] = True

            if j < tj:
                for j1 in range(j, tj):
                    h[ti - 1][j1] = 1
                    marked[ti][j1] = True
            else:
                for j1 in range(tj + 1, j + 1):
                    h[ti - 1][j1 - 1] = 1
                    marked[ti][j1] = True
        else:
            if j < tj:
                for j1 in range(j, tj):
                    h[i - 1][j1] = 1
                    marked[i][j1] = True
            else:
                for j1 in range(tj + 1, j + 1):
                    h[i - 1][j1 - 1] = 1
                    marked[i][j1] = True

            if i < ti:
                for i1 in range(i, ti):
                    v[i1][tj - 1] = 1
                    marked[i1][tj] = True
            else:
                for i1 in range(ti + 1, i + 1):
                    v[i1 - 1][tj - 1] = 1
                    marked[i1][tj] = True

    return h, v
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
def get_id(x,y):
    return x*W+y

h = [list(map(int,input())) for i in range(H-1)]
w = [list(map(int,input())) for i in range(H)]
uf = Unionfind(H*W)

K = int(input())
SD = []
for i in range(K):
    sd = list(map(int,input().split())) + [i]
    SD.append(sd)

event_in = [[] for i in range(T+1)]
event_out = [[] for i in range(T+1)]
for s,d,i in SD:
    event_in[s].append([s,d,i])
    event_out[d].append([d,s,i])

def make_graph(h,w):
    e = [[[] for i in range(W)] for j in range(H)]

    for i in range(H-1):
        nh = h[i]
        for j in range(W):
            if nh[j] == 0:
                e[i][j].append([i+1,j])
                e[i+1][j].append([i,j])

    for i in range(H):
        nw = w[i]

        for j in range(W-1):
            if nw[j] == 0:
                e[i][j].append([i,j+1])
                e[i][j+1].append([i,j])

    return e


def make_field_bfs(h,w):

    e = make_graph(h,w)

    field = [[0]*W for i in range(H)]

    dist = [[inf]*W for i in range(H)]
    lis = [[] for i in range(H*W)]

    q = deque([[SX,SY]])
    dist[SX][SY] =0
    while q:
        x,y = q.popleft()
        lis[dist[x][y]].append([x,y])

        for nx,ny in e[x][y]:
            if dist[nx][ny] > dist[x][y] + 1:
                q.append([nx,ny])
                dist[nx][ny] = dist[x][y] + 1

    size_lim = 10

    def add_line(x,y,dx,dy,f):

        while True:
            field[x][y] = f

            ok = 0
            
            for nx,ny in e[x][y]:
                if field[nx][ny] == 0 and (x+dx,y+dy) == (nx,ny):
                    ok = 1
            
            if ok:            
                x,y = x+dx,y+dy
        
            else:
                break
        return x,y

    def f_line(x,y,dx,dy):

        # print(f"f line x = {x} y = {y} dx = {dx} dy = {dy}")
        cand = []   
        bx,by = x,y
        while True:
            field[x][y] = 2
            ok = 0
            for nx,ny in e[x][y]:
                if field[nx][ny] == 0 and (x+dx,y+dy) == (nx,ny):
                    ok = 1

                if field[nx][ny] == 0:
                    cand.append([nx,ny])
            
            if ok:
                nx,ny = x+dx,y+dy
                uf.union(get_id(x,y),get_id(nx,ny))
                x,y = nx,ny
        
            else:
                lx,ly = x,y
                break

        dx,dy = -dx,-dy
        x,y = bx,by
        while True:
            field[x][y] = 2
            ok = 0
            for nx,ny in e[x][y]:
                if field[nx][ny] == 0 and (x+dx,y+dy) == (nx,ny):
                    ok = 1

                if field[nx][ny] == 0:
                    cand.append([nx,ny])
            
            if ok:
                nx,ny = x+dx,y+dy
                uf.union(get_id(x,y),get_id(nx,ny))
                x,y = nx,ny
        
            else:
                rx,ry = x,y
                break
        
        # print(f"f line x = {x} y = {y} dx = {dx} dy = {dy} lx = {lx} ly = {ly} rx = {rx} ry = {ry}")
        for nx,ny in cand:
            if field[nx][ny] == 0:
                field[nx][ny] = 1
        return (lx+rx)//2,(ly+ry)//2

    def add_field(x,y,NXY,length):
        assert len(NXY) == len(length) == 2

        if length[0] < length[1]:
            length[0],length[1] = length[1],length[0]
            NXY[0],NXY[1] = NXY[1],NXY[0]

        if length[0] > 10 and length[1] >= 4:
        # if length[0] > 10 and length[1] > 1:
            length[0],length[1] = length[1],length[0]
            NXY[0],NXY[1] = NXY[1],NXY[0]

        nx,ny = NXY[0]
        dx,dy = nx-x,ny-y
        rdx,rdy = -dx,-dy

        if dx > 0 or dy > 0:
            dx,dy,rdx,rdy = rdx,rdy,dx,dy

        posx,posy = x,y

        lx,ly = add_line(posx,posy,dx,dy,0)
        rx,ry = add_line(posx,posy,rdx,rdy,0)

        nx,ny = NXY[1]

        lx2,ly2 = add_line(nx,ny,dx,dy,0)
        rx2,ry2 = add_line(nx,ny,rdx,rdy,0)

        if (lx2 <= lx and rx <= rx2 and ly == ry) or (ly2 <= ly and ry <= ry2 and lx == rx):
            cx,cy = f_line(nx,ny,dx,dy)
            return cx,cy

        cx,cy = f_line(posx,posy,dx,dy)

        return cx,cy
                    
    CXY = []
    for i in range(1,H*W)[::-1]:

        for x,y in lis[i]:

            f = field[x][y]
            
            if f:
                continue


            NXY = []
            # print(f"X = {x} Y = {y}")
            nex = 0
            for nx,ny in e[x][y]:
                if field[nx][ny] == 0:
                    NXY.append([nx,ny])
                elif field[nx][ny] == 2:
                    nex = 1
            # print(f"NXY = {NXY}")
            assert len(NXY) < 3

            if len(NXY) == 0:
                if nex:
                    field[x][y] = 1
                else:
                    field[x][y] = 2
                    CXY.append([x,y])
                continue
            if len(NXY) == 1:
                nx,ny = NXY[0]
                dx,dy = nx-x,ny-y
                cx,cy = f_line(nx,ny,dx,dy)
                CXY.append([cx,cy])

                continue


            length = []
            for nx,ny in NXY:

                dx,dy = nx-x,ny-y

                posx,posy = x,y
                num = 0
                assert 0 <= posx < H and 0 <= posy < W
                while True:
                    if field[posx][posy] == 0:
                        num += 1
                    else:
                        break

                    ok = 0
                    for nx,ny in e[posx][posy]:
                        if field[nx][ny] == 0 and (posx+dx,posy+dy) == (nx,ny):
                            ok = 1

                    if ok:
                        posx,posy = posx+dx,posy+dy
                
                    else:
                        break

                length.append(num)

            cx,cy = add_field(x,y,NXY,length)
            CXY.append([cx,cy])

    field[SX][SY] = 2
    CXY.append([SX,SY])
    dist = [[inf]*W for i in range(H)]
    par = [[-1]*W for i in range(H)]

    q = deque([[SX,SY]])
    dist[SX][SY] =0
    while q:
        x,y = q.popleft()

        for nx,ny in e[x][y]:
            f = 1
            if dist[nx][ny] > dist[x][y] + f:
                q.append([nx,ny])
                dist[nx][ny] = dist[x][y] + f
                par[nx][ny] = [x,y]

    CXY = [[dist[cx][cy],cx,cy] for cx,cy in CXY]
    CXY.sort()

    def bfs_dist_update(cx,cy,field,e):

        dist = [[inf]*W for i in range(H)]

        par = [[-1]*W for i in range(H)]
        # print(f"cx = {cx} cy = {cy}")
        q = deque([[cx,cy]])
        min_cost = inf
        mx,my = -1,-1

        dist[cx][cy] = 0
        while q:
            x,y = q.popleft()

            if uf.same(get_id(x,y),get_id(SX,SY)):
                if min_cost > dist[x][y]:
                    min_cost = dist[x][y]
                    mx,my = x,y
                

            for nx,ny in e[x][y]:
                f = field[nx][ny] != 2
                f += 1
                if dist[nx][ny] > dist[x][y] + f:
                    q.append([nx,ny])
                    dist[nx][ny] = dist[x][y] + f
                    par[nx][ny] = [x,y]

        assert mx != -1
        x,y = mx,my
        while True:
            field[x][y] = 2
            px,py = par[x][y]
            uf.union(get_id(x,y),get_id(px,py))
            
            x,y = px,py
            if uf.same(get_id(x,y),get_id(cx,cy)):
                break
        return


    for _,cx,cy in CXY:
        if uf.same(get_id(cx,cy),get_id(SX,SY)):
            continue
        bfs_dist_update(cx,cy,field,e)
    return field,e


def make_field_greedy(h,w):

    h,w = gen_walls(1,H,W,h,w)
    e = make_graph(h,w)
    field = [[0]*W for i in range(H)]

    field[SX][SY] = 2

    for x,y in e[SX][SY]:
        field[x][y] = 1

    par_root = [[[] for i in range(W)] for j in range(H)]

    while True:

        x,y = -1,-1
        best = -1
        root = -1
        parx,pary = -1,-1
        for i in range(H):
            for j in range(W):
                if field[i][j] != 2:
                    continue
                
                if par_root[i][j] != []:
                    px,py = par_root[i][j]
                else:
                    px,py = i,j

                
                for nx,ny in e[i][j]:
                    now = -1

                    for nnx,nny in e[nx][ny]:
                        if field[nnx][nny] == 0:
                            now += 1

                    match = 0

                    if len(e[nx][ny]) == 4:
                        now *= 2
                    if abs(px-nx) == 0 or abs(py-ny) == 0:
                        match = 1
                    if best < now:
                        best = now
                        x,y = nx,ny
                        root = match
                        parx,pary = i,j
                    
                    elif best == now:
                        if root == 0 and match:
                            x,y = nx,ny
                            root = match
                            parx,pary = i,j
        
        if best == -1:
            break

        field[x][y] = 2
        par_root[x][y] = [parx,pary]
        for nx,ny in e[x][y]:
            if field[nx][ny] == 0:
                field[nx][ny] = 1

    return field,e



def bfs_field(field,e):

    par = [[[] for i in range(W)] for j in range(H)]
    child = [[[] for i in range(W)] for j in range(H)]
    dist = [[inf]*W for i in range(H)]
    dist_bfs = [[inf]*W for i in range(H)]

    q = deque([[SX,SY]])

    dist_bfs[SX][SY] = 0
    while q:
        x,y = q.popleft()
        d = dist_bfs[x][y]
        for nx,ny in e[x][y]:

            if dist_bfs[nx][ny] > d+1:
                par[nx][ny] = [[x,y]]
                dist_bfs[nx][ny] = d+1

                if field[nx][ny] == 2:
                    q.append([nx,ny])
            
    for i in range(H):
        for j in range(W):
            if par[i][j] == []:
                continue
            px,py = par[i][j][0]
            child[px][py].append([i,j])

    dist = [[inf]*W for i in range(H)]

    dist[SX][SY] = 0
    q = deque([[SX,SY]])
    dist_max = 0
    while q:
        x,y = q.pop()
        d = dist[x][y]
        for nx,ny in child[x][y]:
            if dist[nx][ny] != inf:
                continue
            dist_max += 1

            if field[nx][ny] == 1:
                dist[nx][ny] = dist_max
            elif field[nx][ny] == 2:
                dist[nx][ny] = dist_max
                q.append([nx,ny])

    return dist,dist_max,par,child


def get_score(ans):
    count = 0
    for k,i,j,s in ans:

        s,d,_ = SD[k-1]
        count += d-s+1

    return 10**6 * count // (H*W*T)
def solve_back(field,dist,dist_max,par,child):
    harvest = [[inf]*W for i in range(H)]

    def get_min(x,y,d):
        assert field[x][y] == 2

        harvest_min = 0

        for nx,ny in child[x][y]:
            if harvest[nx][ny] == inf:
                return inf
            harvest_min = max(harvest_min,harvest[nx][ny])

        return harvest_min


    def evaluate(x,y,s,d):
        
        dist_eval = dist[x][y] * inf // dist_max
        T_eval = (T-s) * inf // T

        distT_eval = abs(dist_eval-T_eval)//5
        
        if field[x][y] == 2:
            # return inf
            har_min = get_min(x,y,s)

            if har_min == inf:
                return inf

            if har_min > s:
                return inf

            if s == har_min:
                return 0
            value = (s - har_min)*T + distT_eval

            return value

        elif field[x][y] == 1:

            value = s  + distT_eval
            return value




    def search(s,d,i,h):
        for x in range(H):
            for y in range(W):
                if harvest[x][y] != inf:
                    continue

                value = evaluate(x,y,s,d)
                if value == inf:
                    continue
                heappush(h,[value,i,x,y])

        return h

    pos = [[-1,-1,-1] for i in range(K)]

    ans = []

    for day in range(1,T+1)[::-1]:

        h = []
        event_out[day].sort()

        for d,s,ind in event_out[day]:

            h = search(s,d,ind,[])

            if h == []:
                continue
            _,ind,x,y = heappop(h)
            assert harvest[x][y] == inf

            pos[ind] = [x,y,s]

            harvest[x][y] = s 

        
        for s,d,ind in event_in[day]:
            if pos[ind] == [-1,-1,-1]:
                continue
            x,y,_ = pos[ind]
            harvest[x][y] = inf


    for i in range(K):
        if pos[i] != [-1,-1,-1]:
            ans.append([i+1]+pos[i])

    return ans


def solve_front(field,dist,dist_max,par,child):

    harvest = [[-1]*W for i in range(H)]

    def get_min(x,y,d):
        assert field[x][y] == 2

        harvest_min = inf

        for nx,ny in child[x][y]:
            if harvest[nx][ny] == -1:
                return inf
            harvest_min = min(harvest_min,harvest[nx][ny])

        return harvest_min


    def evaluate(x,y,s,d):
        
        dist_eval = dist[x][y] * inf // dist_max
        T_eval = d * inf // T

        distT_eval = abs(dist_eval-T_eval)//5
        
        if field[x][y] == 2:
            # return inf
            har_min = get_min(x,y,d)
            if har_min == inf:
                return inf

            if har_min< d:
                return inf
            if d == har_min:
                return 0
            value = (har_min - d)*T + distT_eval

            return value

        elif field[x][y] == 1:

            value = d  + distT_eval
            return value




    def search(s,d,i,h):
        for x in range(H):
            for y in range(W):
                if harvest[x][y] != -1:
                    continue

                value = evaluate(x,y,s,d)
                if value == inf:
                    continue
                heappush(h,[value,i,x,y])

        return h


    pos = [[-1,-1,-1] for i in range(K)]

    ans = []

    for day in range(1,T+1):

        h = []
        event_in[day].sort(reverse=True)

        for s,d,ind in event_in[day]:

            h = search(s,d,ind,[])

            if h == []:
                continue
            
            _,ind,x,y = heappop(h)
            assert harvest[x][y] == -1

            pos[ind] = [x,y,s]
            s,d,_ = SD[ind]
            
            harvest[x][y] = d
    

        for d,s,ind in event_out[day]:
            x,y,_ = pos[ind]
            if x != -1:
                harvest[x][y] = -1


    for i in range(K):
        if pos[i] != [-1,-1,-1]:
            ans.append([i+1]+pos[i])

    return ans



def update_ans(ans,best_score,ans_new,now_score):

    if now_score > best_score:
        return ans_new,now_score
    else:
        return ans,best_score

best_score = 0
ans = []


field_bfs,e_bfs = make_field_bfs(h,w)

field_greedy,e_greedy = make_field_greedy(h,w)

dist,dist_max,par,child = bfs_field(field_bfs,e_bfs)

ans_front = solve_front(field_bfs,dist,dist_max,par,child)
front_score = get_score(ans_front)
ans,best_score = update_ans(ans,best_score,ans_front,front_score)

ans_back = solve_back(field_bfs,dist,dist_max,par,child)
back_score = get_score(ans_back)
ans,best_score = update_ans(ans,best_score,ans_back,back_score)


dist,dist_max,par,child = bfs_field(field_greedy,e_greedy)

ans_front = solve_front(field_greedy,dist,dist_max,par,child)
front_score = get_score(ans_front)
ans,best_score = update_ans(ans,best_score,ans_front,front_score)

ans_back = solve_back(field_greedy,dist,dist_max,par,child)
back_score = get_score(ans_back)
ans,best_score = update_ans(ans,best_score,ans_back,back_score)
# print(best_score)
print(len(ans))

for k,i,j,s in ans:
    print(k,i,j,s)