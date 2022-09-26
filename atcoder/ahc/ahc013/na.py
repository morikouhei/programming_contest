import random
import sys
from copy import deepcopy
from collections import deque
random.seed(1)


N, K = [int(v) for v in input().split(" ")]
C = [[int(x) for x in input()] for i in range(N)]
C_true = deepcopy(C)

used_path = [[0]*N for i in range(N)]
used_path_base = [[0]*N for i in range(N)]
used_path2 = [[-1]*N for i in range(N)]
last_vis = [[-1]*N for i in range(N)]
last_vis2 = [[-1]*N for i in range(N)]
dist_vis = [[-1]*N for i in range(N)]
joint_path = [[0]*N for i in range(N)]
lim = 100*K
cash = 0
cash2 = 0
dX = [1,0,-1,0]
dY = [0,1,0,-1]
def pos2ind(x,y):
    return x*N+y

def ind2pos(ind):
    return divmod(ind,N)

def size2score(size):
    return size*(size-1)//2

def can_connect(i, j, dind):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
    while 0 <= i2 < N and 0 <= j2 < N:

        if used_path[i2][j2]:
            return -1,-1

        if C[i2][j2] == cid:
            return i2,j2

        if C[i2][j2] == 0:
            i2 += dX[dind]
            j2 += dY[dind]
            continue
        
        return -1,-1
    return -1,-1

def check_connect(i, j, dind):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
    target_list = []
    while 0 <= i2 < N and 0 <= j2 < N:

        if C[i2][j2] == cid:
            return i2,j2,target_list

        
        if used_path_base[i2][j2]:
            return -1,-1,[]


        if C[i2][j2] == 0:
            if joint_path[i2][j2]:
                if used_path[i2][j2]:
                    return -1,-1,[]
                else:
                    return i2,j2,target_list
            else:
                if used_path[i2][j2]:
                    target_list.append([i2,j2])
            i2 += dX[dind]
            j2 += dY[dind]
            continue
        
        return -1,-1,[]
    return -1,-1,[]

def check_connect2(i, j, dind,cash):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
  
    while 0 <= i2 < N and 0 <= j2 < N:
        # print(i2,j2,i,j,used_path[i2][j2],cash)
        if used_path[i2][j2] != cash:
            return -1,-1
        if C[i2][j2] == cid:
            return i2,j2

        if C[i2][j2] == 0:
            i2 += dX[dind]
            j2 += dY[dind]
            continue
        
        return -1,-1
    return -1,-1

def can_connect_greedy(i, j, dind):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
    while 0 <= i2 < N and 0 <= j2 < N:

        if C[i2][j2] == cid:
            return i2,j2

        if used_path[i2][j2]:
            return -1,-1

        if C[i2][j2] == 0:
            i2 += dX[dind]
            j2 += dY[dind]
            continue
        
        return -1,-1
    return -1,-1
def do_connect(i, j, dind,cashs=-1):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    if cashs == -1:
        cashs = C[i][j]
    cid = C[i][j]
    used_path[i][j] = cashs
    while 0 <= i2 < N and 0 <= j2 < N:
        used_path[i2][j2] = cashs
        if C[i2][j2] == cid:
            return
        i2 += dX[dind]
        j2 += dY[dind]
        
    return

def do_connect2(i, j, dind,cash):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
    used_path2[i][j] = cash
    while 0 <= i2 < N and 0 <= j2 < N:
        used_path2[i2][j2] = cash
        if C[i2][j2] == cid:
            return
        i2 += dX[dind]
        j2 += dY[dind]
        
    return


def do_connect_greedy(i, j, dind):
    i2 = i + dX[dind]
    j2 = j + dY[dind]
    cid = C[i][j]
    used_path[i][j] = cid
    while 0 <= i2 < N and 0 <= j2 < N:
        
        if C[i2][j2] == cid:
            return

        used_path[i2][j2] = cid
        i2 += dX[dind]
        j2 += dY[dind]
        
    return


def bfs(x,y,return_vis=False):
    global cash
    if used_path[x][y]:
        if return_vis == False:
            return 0
        else:
            return 0,[]
    cid = C[x][y]
    if cid == 0:
        if return_vis == False:
            return 0
        else:
            return 0,[]

    q = [[x,y]]
    last_vis[x][y] = cash
    gsum = 1
    if return_vis:
        vis_list = []
        vis_list.append([x,y])
    while q:
        nx,ny = q.pop()

        for dind in range(4):
            i2,j2 = can_connect(nx,ny,dind)
            if i2 == -1:
                continue
            if last_vis[i2][j2] == cash:
                continue
            last_vis[i2][j2] = cash
            q.append([i2,j2])
            if return_vis:
                vis_list.append([i2,j2])
            gsum += 1

    cash += 1
    if return_vis == False:
        return gsum
    else:
        return gsum,vis_list
    
def bfs_connect(x,y):
    global cash

    connects = []
    if used_path[x][y]:
        return connects
    cid = C[x][y]

    if cid == 0:
        return connects

    q = [[x,y]]
    last_vis[x][y] = cash
    gsum = 1

    while q:
        nx,ny = q.pop()

        for dind in range(4):
            i2,j2 = can_connect(nx,ny,dind)
            
            if i2 == -1:
                continue
            if last_vis[i2][j2] == cash:
                continue
            connects.append([nx,ny,i2,j2])
            do_connect(nx,ny,dind)
            q.append([i2,j2])
    cash += 1
    return connects



def check_join_search(x,y,c):
    s = set()
    if C[x][y] != 0:
        return s
    for dind in range(4):
        i2 = x + dX[dind]
        j2 = y + dY[dind]
        while 0 <= i2 < N and 0 <= j2 < N:

            if C[i2][j2] == 0:
                i2 += dX[dind]
                j2 += dY[dind]
                continue
            if C[i2][j2] == c:
                s.add((i2,j2))
            break

    return s

def check_join_search2(x,y,c):
    s = set()

    for dind in range(4):
        i2 = x + dX[dind]
        j2 = y + dY[dind]
        while 0 <= i2 < N and 0 <= j2 < N:
            if used_path_base[i2][j2]:
                break
            if C[i2][j2] == 0:
                i2 += dX[dind]
                j2 += dY[dind]
                continue
            if C[i2][j2] == c:
                s.add((i2,j2))
            break

    return s
        
def check_join(vis_j,vis_k,c,return_list=False):
    returns = []
    for x,y in vis_j:
        
        for nx,ny in vis_k:

            s1 = check_join_search(x,ny,c)
            if (x,y) in s1 and (nx,ny) in s1:
                if return_list == False:
                    return True
                else:
                    returns.append([x,ny])

            s1 = check_join_search(nx,y,c)
            if (x,y) in s1 and (nx,ny) in s1:
                
                if return_list == False:
                    return True
                else:
                    returns.append([nx,y])
            
    if return_list == False:
        return False
    else:
        return returns

class Result:

    def __init__(self, moves, connects):
        self.moves = moves
        self.connects = connects


def print_answer(res: Result):
    assert len(res.moves)+len(res.connects) <= lim
    print(len(res.moves))
    for arr in res.moves:
        print(*arr)
    print(len(res.connects))
    for arr in res.connects:
        print(*arr)


def check_answer(res,C):
    C_test = deepcopy(C_true)

    for x,v in enumerate(res.moves):
        # print(v)
        i, j, i2, j2 = v

        assert C_test[i][j]+C_test[i2][j2],v
        C_test[i2][j2],C_test[i][j] = C_test[i][j],C_test[i2][j2]

    if C != C_test:
        # for i in range(N):
        #     for j in range(N):
        #         if C[i][j] != C_test[i][j]:
        #             print(i,j)
    
        # for c in C:
        #     print(*c,sep="")

        # print()

        # for c in C_test:
        #     print(*c,sep="")
        return -1
    return True
    assert C == C_test


class Unionfind:
 
    def __init__(self,n):
        self.uf = [-1]*(n**2)
        self.n = n
 
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


def calc_score(N, K, C, res: Result):

    for v in res.moves:
        # print(v)
        i, j, i2, j2 = v
        if C[i][j]+C[i2][j2] == 0:

            return -1
        assert C[i][j]+C[i2][j2]
        C[i2][j2],C[i][j] = C[i][j],C[i2][j2]


    uf = Unionfind(N**2)
    temp1 = [[0]*N for i in range(N)]
    temp2 = [[0]*N for i in range(N)]
    for v in res.connects:
        i, j, i2, j2 = v
        if C[i][j] == 0 or C[i2][j2] == 0:
            return -1
        assert 1 <= C[i][j] <= K
        assert 1 <= C[i2][j2] <= K
        dx,dy = i2-i,j2-j
        if dx > 0:
            dx = 1
        elif dx < 0:
            dx = -1
        if dy > 0:
            dy = 1
        elif dy < 0:
            dy = -1

        assert temp2[i][j] == 0
        assert temp2[i2][j2] == 0
        ni,nj = i+dx,j+dy
        while (ni,nj) != (i2,j2):
            assert temp1[ni][nj] == 0
            assert temp2[ni][nj] == 0
            temp2[ni][nj] = 1
            ni,nj = ni+dx,nj+dy
        temp1[i][j] = temp1[i2][j2] = 1
        uf.union(pos2ind(i,j), pos2ind(i2,j2))

    score = 0
    for i in range(N):
        for j in range(N):
            if C[i][j] == 0:
                continue
            ind = pos2ind(i,j)
            if uf.find(ind) == ind:
                score += size2score(uf.size(ind))
                
    return max(score, 0)



def greedy_answer():
    cand = []
    for i in range(N):
        for j in range(N):
            if last_vis[i][j] != -1 or C[i][j] == 0:
                continue
            gsum = bfs(i,j)
            cand.append([gsum,i,j])
    cand.sort(reverse=True)

    moves_lis = []
    connect_lis = []

    for _,x,y in cand:
        connects = bfs_connect(x,y)
        connect_lis += connects

    for i in range(N):
        for j in range(N):
            if used_path[i][j] or C[i][j] == 0:
                continue

            for dind in range(2):
                i2,j2 = can_connect_greedy(i,j,dind)
                if i2 != -1:
                    connect_lis.append([i,j,i2,j2])
                    do_connect_greedy(i,j,dind)

    res = Result(moves_lis,connect_lis)
    temp_score = calc_score(N,K,deepcopy(C),res)
    return res,temp_score


res,temp_score = greedy_answer()



used_path = [[0]*N for i in range(N)]
last_vis = [[-1]*N for i in range(N)]
waiting_set = set()
cash = 0

uf_size = Unionfind(N**2)
cand = [[] for i in range(K+1)]
for i in range(N):
    for j in range(N):
        if last_vis[i][j] != -1 or C[i][j] == 0:
            continue
        gsum,vis_list = bfs(i,j,True)
        if gsum <= 2:
            continue
        for x,y in vis_list:
            uf_size.union(pos2ind(i,j),pos2ind(x,y))
        cand[C[i][j]].append([gsum,i,j,vis_list])

uf_size_base = deepcopy(uf_size)

cand_new = []
can_join_set = {}
for i in range(1,K+1):
    
    li = len(cand[i])
    for j in range(li):
        cand_j = cand[i][j]
        vis_j = cand[i][j][3]
        for k in range(j):
            cand_k = cand[i][k]
            vis_k = cand[i][k][3]
            join_list = check_join(vis_j,vis_k,i,True)
            if join_list != []:
                for x,y in join_list:
                    joint_path[x][y] = 1
                x,y = cand_j[1],cand_j[2]
                nx,ny = cand_k[1],cand_k[2]
                uf_size.union(pos2ind(x,y),pos2ind(nx,ny))

    for j in range(li):
        x,y = cand[i][j][1],cand[i][j][2]
        if uf_size.find(pos2ind(x,y)) == uf_size_base.find(pos2ind(x,y)):
            cand_new.append([uf_size.size(pos2ind(x,y)),x,y])

cand_new.sort(reverse=True)

C_base = deepcopy(C)


def bfs_join(point_list,c):
    global cash
    global C,C_base
    q = deque([])
    for x,y in point_list:
        if used_path[x][y]:
            continue
        dist_vis[x][y] = 0
        q.append([x,y])
        last_vis[x][y] = cash

    while q:
        nx,ny = q.popleft()

        for dind in range(4):
            nnx,nny = nx+dX[dind],ny+dY[dind]
            if 0 <= nnx < N and 0 <= nny < N and last_vis[nnx][nny] != cash:
                if C[nnx][nny] == C_base[nnx][nny]:
                    if C[nnx][nny] == 0:
                        last_vis[nnx][nny] = cash
                        dist_vis[nnx][nny] = dist_vis[nx][ny]+1
                        q.append([nnx,nny])
                    elif C[nnx][nny] == c:
                        if uf_size_base.size(pos2ind(nnx,nny)) == 1:
                            last_vis[nnx][nny] = cash
                            dist_vis[nnx][nny] = dist_vis[nx][ny]+1
                            moves = []
                            x,y = nnx,nny
                            while dist_vis[x][y] != 0:
                                for dind in range(4):
                                    nnx,nny = x+dX[dind],y+dY[dind]
                                    if 0 <= nnx < N and 0 <= nny < N and last_vis[nnx][nny] == cash and dist_vis[nnx][nny] == dist_vis[x][y]-1:
                                        moves.append([x,y,nnx,nny])
                                        x,y = nnx,nny
                                        break
                            cash += 1
                            return moves,True

                # else:
                #     if C[nnx][nny] == 0:
                #         last_vis[nnx][nny] = cash
                #         dist_vis[nnx][nny] = dist_vis[nx][ny]+1
                        # q.append([nnx,nny])
    cash += 1        
    return [],False

def bfs_join2(point_list,c):
    global cash2

    q = deque([])
    for x,y in point_list:
        dist_vis[x][y] = 0
        q.append([x,y])
        last_vis2[x][y] = cash2
        # print(x,y,cash)

    while q:
        nx,ny = q.popleft()

        for dind in range(4):
            nnx,nny = nx+dX[dind],ny+dY[dind]
            if 0 <= nnx < N and 0 <= nny < N and last_vis2[nnx][nny] != cash2:
                if (nnx,nny) not in waiting_set:
                    if C[nnx][nny] == 0:
                        last_vis2[nnx][nny] = cash2
                        dist_vis[nnx][nny] = dist_vis[nx][ny]+1
                        q.append([nnx,nny])
                    elif C[nnx][nny] == c:
                        if uf_size_base.size(pos2ind(nnx,nny)) == 1:
                            last_vis2[nnx][nny] = cash2
                            dist_vis[nnx][nny] = dist_vis[nx][ny]+1
                            moves = []
                            x,y = nnx,nny
                            while dist_vis[x][y] != 0:
                                for dind in range(4):
                                    nnx,nny = x+dX[dind],y+dY[dind]
                                    if 0 <= nnx < N and 0 <= nny < N and last_vis2[nnx][nny] == cash2 and dist_vis[nnx][nny] == dist_vis[x][y]-1:
                                        moves.append([x,y,nnx,nny])
                                        x,y = nnx,nny
                                        break
                            cash2 += 1
                            return moves,True

    cash2 += 1

    return [],False

def bfs_check(x,y):
    
    global cash,C,C_base

    moves = []
    if used_path2[x][y] == cash:
        return [],[]

    if used_path[x][y]:
        return [],[]
    cid = C[x][y]

    if cid == 0:
        return [],[]

    q = [[x,y]]
    last_vis[x][y] = cash

    temp_pos_all = []
    while q:
        nx,ny = q.pop()

        for dind in range(4):
            i2,j2,target_list = check_connect(nx,ny,dind,cash) ### check?
            
            if i2 == -1:
                continue
            if last_vis[i2][j2] == cash:
                continue
            
            join_flg = True
            temp_moves = []
            temp_pos = []

            for tx,ty in target_list:

                cand_move,flg = bfs_join2([[tx,ty]],cid)
                if flg == False:
                    join_flg = False
                    break

                tx,ty = cand_move[0][:2]
                lx,ly = cand_move[-1][2:]
                temp_moves.append(cand_move)
                temp_pos.append([tx,ty,lx,ly])
                # print(tx,ty,lx,ly,len(temp_moves))
                C[lx][ly],C[tx][ty] = C[tx][ty],C[lx][ly]

            if join_flg == False:
                for tx,ty,lx,ly in temp_pos:
                    C[lx][ly],C[tx][ty] = C[tx][ty],C[lx][ly]
            else:
                # for t,cand_move in zip(temp_pos,temp_moves):
                    # print(t,len(cand_move),len(target_list),nx,ny,i2,j2)
                    # for l in cand_move:
                    #     print(*l)
                for t in temp_pos:
                    temp_pos_all.append(t)
                # for tx,ty,lx,ly in temp_pos:
                #     C_base[lx][ly],C_base[tx][ty] = C_base[tx][ty],C_base[lx][ly]
         
                do_connect2(nx,ny,dind,cash)
                for cand_move in temp_moves:
                    # if [4,14,3,14] in cand_move:
                    #     print("FIND")
                    #     print(cand_move)
                    moves.append(cand_move)
                last_vis[i2][j2] = cash
                q.append([i2,j2])
    cash += 1
    return moves,temp_pos_all



def update_connect_joint(x,y,cash):
    temp_connects = []

    done_set = set()
    # print(x,y,cash,"connect")
    q = deque([])
    q.append([x,y])
    done_set.add((x,y))

    while q:
        nx,ny = q.popleft()
        # print(nx,ny)
        for dind in range(4):
            i2,j2 = check_connect2(nx,ny,dind,cash)
            if i2 == -1:
                continue
            # print(nx,ny,i2,j2)
            if (i2,j2) in done_set:
                continue
            temp_connects.append([nx,ny,i2,j2])
            done_set.add((i2,j2))
            q.append([i2,j2])

    return temp_connects


def update_connect(x,y,current_lim,c):

    global waiting_set,cash
    cash += 1
    waiting_set = set()
    temp_moves,temp_connects = [],[]

    used_path[x][y] = cash
    q_first = deque([])
    q_first.append([x,y])
    # print(x,y,cash,current_lim)
    gsize = set()
    gsize.add((x,y))
    while True:
        joint_path_list = set()
        while q_first:
            nx,ny = q_first.popleft()
            for dind in range(4):
                i2,j2,target_list = check_connect(nx,ny,dind)

                if i2 == -1:
                    continue

                if used_path[i2][j2]:
                    continue
                
                if C[i2][j2] == 0:
                    joint_path_list.add((i2,j2))
                    continue
                
                join_flg = True
                add_moves = []
                temp_pos = []
                add_nums = 1
                for tx,ty in target_list:

                    cand_move,flg = bfs_join2([[tx,ty]],c)
                    if flg == False:
                        join_flg = False
                        break

                    tx,ty = cand_move[0][:2]
                    lx,ly = cand_move[-1][2:]
                    add_moves.append(cand_move)
                    add_nums += len(cand_move)
                    temp_pos.append([tx,ty,lx,ly])
       
                    C[lx][ly],C[tx][ty] = C[tx][ty],C[lx][ly]
                    waiting_set.add((lx,ly))
                    waiting_set.add((tx,ty))
                    gsize.add((tx,ty))

                if join_flg == False or add_nums + len(gsize) > current_lim:
                    for tx,ty,lx,ly in temp_pos:
                        C[lx][ly],C[tx][ty] = C[tx][ty],C[lx][ly]
                else:
                    for cand_move in add_moves:
                        temp_moves += cand_move
            
                    target_list = [[nx,ny]]+target_list + [[i2,j2]]
                    for i in range(len(target_list)-1):
                        x1,y1 = target_list[i]
                        x2,y2 = target_list[i+1]
                        q_first.append([x2,y2])
                        gsize.add((x2,y2))
                        # temp_connects.append([x1,y1,x2,y2])
                        uf_size_base.union(pos2ind(x1,y1),pos2ind(x2,y2))
                    do_connect(nx,ny,dind,cash)
      
                    # last_vis[i2][j2] = cash
                    # q_first.append([i2,j2])
                    current_lim -= add_nums

                waiting_set = set()

        joint_path_cand = []

        for tx,ty in joint_path_list:
            connect_list = check_join_search2(tx,ty,c)
            size = 0
            done = set()
            for nx,ny in connect_list:
                nind = uf_size_base.find(pos2ind(nx,ny))
                if nind in done:
                    continue
                done.add(nind)
                size += uf_size_base.size(nind)
            if len(done) > 1:
                joint_path_cand.append([size,tx,ty,connect_list])

        joint_path_cand.sort(reverse=True)

        for _,tx,ty,connect_list in joint_path_cand:
            
            done = set()
            for nx,ny in connect_list:
                nind = uf_size_base.find(pos2ind(nx,ny))
                if nind in done:
                    continue
                done.add(nind)
 
            if len(done) == 1:
                continue

            cand_move,flg = bfs_join2([[tx,ty]],c)
            if flg == False or len(cand_move) > current_lim:
                continue

            current_lim -= len(cand_move)
            temp_moves += cand_move
            tx,ty = cand_move[0][:2]
            lx,ly = cand_move[-1][2:]
            C[lx][ly],C[tx][ty] = C[tx][ty],C[lx][ly]

            for nx,ny in connect_list:
                if used_path[nx][ny]:
                    
                    q_first.append([nx,ny])


        if len(q_first) == 0 or current_lim == 0:
            break

    temp_connects = update_connect_joint(x,y,cash)
    return temp_moves,temp_connects,current_lim


def update_new_connect(base_list,current_lim,c):

    new_moves = []
    new_connects = []

    for x,y in base_list:
        if used_path[x][y]:
            continue
        # print(x,y,current_lim)
        temp_moves,temp_connects,current_lim = update_connect(x,y,current_lim,c)
        new_moves += temp_moves
        new_connects += temp_connects
        # print(x,y,current_lim,"after")
    return new_moves,new_connects

moves = []
connects = []

# print(cand_new)
for _,x,y in cand_new:
    # print(x,y)
    used_path_save = deepcopy(used_path)
    C_save = deepcopy(C_base)

    base_list = []
    for i in range(N):
        for j in range(N):
            if uf_size_base.same(pos2ind(x,y),pos2ind(i,j)):
                base_list.append([i,j])


    current_lim = lim - len(moves) - len(connects)
    c = C[x][y]

    new_moves,new_connects = update_new_connect(base_list,current_lim,c)
    moves += new_moves
    connects += new_connects
    used_path_base = deepcopy(used_path)
   
    # print(x,y,C[x][y])
    print_answer(Result(moves,connects))

    # assert C == C_base
    # check_answer(Result(moves,connects),C)

new_res = Result(moves,connects)
# print_answer(new_res)
new_score = calc_score(N,K,deepcopy(C_true),new_res)
# print(new_score)
if new_score > temp_score and len(moves)+len(connects) <= lim and check_answer(new_res,C) != -1:
    res = new_res
    temp_score = new_score

# print(temp_score)
print_answer(res)
print_answer(new_res)
