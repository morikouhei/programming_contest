import time
import random
from heapq import heappop,heappush
from collections import deque
import itertools

random.seed(998244353)
stime = time.time()
TIME_LIM = 2

N = int(input())
N2 = N**2
inf = 10**10

inf2 = 10**20
DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = "RDLU"

def id_2_xy(id):
    return divmod(id,N)

def xy_2_id(x,y):
    return x*N+y

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


class Environment:

    ### input受け取り用 1次元に変換しておく
    def __init__(self):
        self.GRID_SIZE = 4

        self.edges_point = [[] for i in range(N2)]
        self.edges_grid = []
        self.D = [0]*N2
        self.D_sum = 0
        self.D_avg = 0

        self.grid_num = 0
        self.grid_indexes = [-1]*N2
        self.grid_info = []
        self.grid_point_list = []

        self.bfs_dist = []
        self.dijkstra_dist = []
        self.grid_dist = []

        self._input()
        self._make_grid()
        self._make_shortest_root()

    ### input受け取り 移動できる隣接点との辺をはる
    def _input(self):

        H = [list(map(int,input())) for i in range(N-1)]
        V = [list(map(int,input())) for i in range(N)]
        for i in range(N):
            d = list(map(int,input().split()))
            for j in range(N):
                self.D[i*N+j] = d[j]

        self.D_sum = sum(self.D)
        self.D_avg = self.D_sum // N2

        for x in range(N):
            for y in range(N):
                id = xy_2_id(x,y)
                for (dx,dy),dS in zip(DIJ,DIR):
                    nx,ny = x+dx,y+dy

                    if 0 <= nx < N and 0 <= ny < N:
                        if (dx == 0 and V[x][min(y,ny)] == 0) or (dy == 0 and H[min(x,nx)][y] == 0):
                            nid = xy_2_id(nx,ny)
                            self.edges_point[id].append([nid,dS])
  
    ### gridで頂点をグループに分ける グループ毎の頂点の情報や、グループ間の辺をはる
    def _make_grid(self):

        for x in range(N):
            for y in range(N):
                id = xy_2_id(x,y)
                if self.grid_indexes[id] != -1:
                    continue
                
                lx,ly = x,y

                # lx = x//self.GRID_SIZE*self.GRID_SIZE
                # ly = y//self.GRID_SIZE*self.GRID_SIZE
                rx = min(N,lx+self.GRID_SIZE)
                ry = min(N,ly+self.GRID_SIZE)

  
                weight = 0
                num = 0
                q = [id]
                self.grid_indexes[id] = self.grid_num

                while q:
                    pid = q.pop()
                    weight += self.D[pid]
                    num += 1

                    for nid,_ in self.edges_point[pid]:
                        nx,ny = id_2_xy(nid)
                        if lx <= nx < rx and ly <= ny < ry and self.grid_indexes[nid] == -1 :#and max(self.D[pid],self.D[nid])/min(self.D[pid],self.D[nid]) <= 10:
                            self.grid_indexes[nid] = self.grid_num
                            q.append(nid)
                
                self.grid_info.append([self.grid_num,num,weight,weight//num])
                self.edges_grid.append(set())
            
                self.grid_num += 1

        

        self.grid_point_list = [[] for i in range(self.grid_num)]

        for id in range(N2):

            self.grid_point_list[self.grid_indexes[id]].append(id)
            for nid,_ in self.edges_point[id]:
                if self.grid_indexes[id] != self.grid_indexes[nid]:
                    self.edges_grid[self.grid_indexes[id]].add((self.grid_indexes[nid],""))
    
    ### gridのグループまでの最短経路の情報を計算

    def calc_shortest_root(self,grid_indexes):
        bfs_dist = [1<<20]*N2
        dijkstra_dist = [-1]*N2

        q = []

        for id in grid_indexes:
            q.append(id)
            bfs_dist[id] = 0
            dijkstra_dist[id] = self.D[id]

        dis = 0
        while q:

            nq = []

            while q:
                now = q.pop()

                for nex,_ in self.edges_point[now]:

                    if bfs_dist[nex] > dis+1:
                        bfs_dist[nex] = dis+1
                        nq.append(nex)

                    if bfs_dist[nex] == dis+1:
                        dijkstra_dist[nex] = max(dijkstra_dist[now]+self.D[nex],dijkstra_dist[nex])

            q = nq
            dis += 1

        return bfs_dist,dijkstra_dist

    def _make_shortest_root(self):

        self.grid_dist = [[inf]*self.grid_num for i in range(self.grid_num)]
        for grid_id in range(self.grid_num):

            bfs_dist,dijkstra_dist = self.calc_shortest_root(self.grid_point_list[grid_id])
            self.bfs_dist.append(bfs_dist)
            self.dijkstra_dist.append(dijkstra_dist)

            for i,d in enumerate(bfs_dist):
                self.grid_dist[grid_id][self.grid_indexes[i]] = min(self.grid_dist[grid_id][self.grid_indexes[i]],d)

    
    ### ある頂点から grid_id のグループまでのパスを求めて list で返す
    def get_shortest_root(self,now,grid_id):

        root = []
        while self.grid_indexes[now] != grid_id:

            nex_cand = []
            nex_weight = 0
            for nex,_ in self.edges_point[now]:
                if self.bfs_dist[grid_id][nex] == self.bfs_dist[grid_id][now]-1:
                    w = self.dijkstra_dist[grid_id][nex]
                    nex_weight += w
                    nex_cand.append([nex,w])
            
            assert nex_cand

            rnd = random.random()
            cum = 0
            for nex,w in nex_cand:
                cum += w
                if cum/nex_weight < rnd:
                    break

            root.append(nex)
            now = nex

        return root

    def get_shortest_root_blocks(self,pid,block_root):
        grid_id = -1
        best_dist = [inf,-inf]
        for block in block_root:
            dist = [self.bfs_dist[block][pid],self.dijkstra_dist[block][pid]]
            if dist < best_dist:
                best_dist = dist
                grid_id = block


        
        return self.get_shortest_root(pid,grid_id)

    def get_shortest_root_point(self,pid,nex_pos):
        grid_id = self.grid_indexes[nex_pos]

        path = self.get_shortest_root(pid,grid_id)

        dis_dic = {}
        par_dic = {}
        if path:
            pid = path[-1]
        # pid = path[-1]

        for id in self.grid_point_list[grid_id]:
            dis_dic[id] = inf

        dis_dic[pid] = 0
        q = deque([pid])

        while q:
            id = q.popleft()
            d = dis_dic[id]
            if id == nex_pos:
                break
  
            for nid,_ in self.edges_point[id]:
                if self.grid_indexes[nid] == grid_id and dis_dic[nid] > d+1:
                    q.append(nid)
                    dis_dic[nid] = d+1
                    par_dic[nid] = id


        nid = nex_pos

        moves = []
        while nid != pid:
            moves.append(nid)
            nid = par_dic[nid]

        for mv in moves[::-1]:
            path.append(mv)


        
        return path

environment = Environment()


class Solver:

    def __init__(self):

        self.score = inf2
        self.T = -1
        self.score_list = []
        self.score_avg = 0

        self.grid_ans = []
        self.ans = []

        self.grid_info = environment.grid_info[:]

        self.has_cluster = [0]*environment.grid_num
        self.cluster_num = 0
        self.cluster_indexes = [-1]*N2
        self.cluster_d_sum = [[0,0,i] for i in range(environment.grid_num)]
        self.cluster_grid_list = [[] for i in range(environment.grid_num)]
        self.cluster_point_list = [[] for i in range(environment.grid_num)]
        self.bfs_dist = [[] for i in range(environment.grid_num)]
        self.dijkstra_dist = [[] for i in range(environment.grid_num)]

        self.cluster_dist = []
        self.uf = Unionfind(environment.grid_num)



        # self._build_cluster_info()
        

    def _build_cluster_info(self):

        D_avg = environment.D_avg

        for i,d in enumerate(environment.D):
            if d/D_avg >= 3:
                self.has_cluster[environment.grid_indexes[i]] = 1
        
        for i in range(environment.grid_num):
            if self.has_cluster[i] == 0:
                continue

            for ni,_ in environment.edges_grid[i]:
                if self.has_cluster[ni]:
                    self.uf.union(i,ni)

        for i in range(environment.grid_num):
            if self.has_cluster[i] == 0:
                continue

            p = self.uf.find(i)

            if p == i:
                self.cluster_num += 1

            self.cluster_d_sum[p][0] += self.grid_info[i][2]
            self.cluster_d_sum[p][1] += self.grid_info[i][1]
            self.cluster_grid_list[p].append(i)
            
            for ind in environment.grid_point_list[i]:
                self.cluster_point_list[p].append(ind)
                self.cluster_indexes[ind] = p
                
            
        self.cluster_d_sum.sort(reverse=True)

        self.cluster_dist = [[inf]*environment.grid_num for i in range(environment.grid_num)]
        for i in range(environment.grid_num):
            self.cluster_dist[i][i] = 0

        
        for i in range(min(5,self.cluster_num)):
            _,_,p = self.cluster_d_sum[i]

            bfs_dist,dijkstra_dist = environment.calc_shortest_root(self.cluster_point_list[p])
            self.bfs_dist[p] = bfs_dist
            self.dijkstra_dist[p] = dijkstra_dist

            for ind,d in enumerate(bfs_dist):
                np = self.cluster_indexes[ind]
                if np != -1:
                    self.cluster_dist[p][np] = min(self.cluster_dist[p][np],d)


    def _build_cluster_info2(self):
        
        self.has_cluster = [0]*environment.grid_num
        self.cluster_num = 0
        self.cluster_indexes = [-1]*N2
        self.cluster_d_sum = [[0,0,i] for i in range(environment.grid_num)]
        self.cluster_grid_list = [[] for i in range(environment.grid_num)]
        self.cluster_point_list = [[] for i in range(environment.grid_num)]
        self.bfs_dist = [[] for i in range(environment.grid_num)]
        self.dijkstra_dist = [[] for i in range(environment.grid_num)]

        self.cluster_dist = []
        self.uf = Unionfind(environment.grid_num)

        score_avg = self.score_avg
        
        for i,d in enumerate(self.score_list):
            if d/score_avg >= 3:
                self.has_cluster[environment.grid_indexes[i]] = 1
        
        for i in range(environment.grid_num):
            if self.has_cluster[i] == 0:
                continue

            for ni,_ in environment.edges_grid[i]:
                if self.has_cluster[ni]:
                    self.uf.union(i,ni)

        for i in range(environment.grid_num):
            if self.has_cluster[i] == 0:
                continue

            p = self.uf.find(i)

            if p == i:
                self.cluster_num += 1

            for id in environment.grid_point_list[i]:
                # self.cluster_d_sum[p][0] += environment.D[id]
                self.cluster_d_sum[p][0] += self.score_list[id]
                self.cluster_d_sum[p][1] += 1
            # self.cluster_d_sum[p][0] += self.grid_info[i][2]
            # self.cluster_d_sum[p][1] += self.grid_info[i][1]
            self.cluster_grid_list[p].append(i)
            
            for ind in environment.grid_point_list[i]:
                self.cluster_point_list[p].append(ind)
                self.cluster_indexes[ind] = p
                
            
        self.cluster_d_sum.sort(reverse=True)

        self.cluster_dist = [[inf]*environment.grid_num for i in range(environment.grid_num)]
        for i in range(environment.grid_num):
            self.cluster_dist[i][i] = 0

        
        for i in range(min(5,self.cluster_num)):
            _,_,p = self.cluster_d_sum[i]

            bfs_dist,dijkstra_dist = environment.calc_shortest_root(self.cluster_point_list[p])
            self.bfs_dist[p] = bfs_dist
            self.dijkstra_dist[p] = dijkstra_dist

            for ind,d in enumerate(bfs_dist):
                np = self.cluster_indexes[ind]
                if np != -1:
                    self.cluster_dist[p][np] = min(self.cluster_dist[p][np],d)


    def make_cluster_group(self,cluster_num):


        cluster_list = [ind for _,_,ind in self.cluster_d_sum[:cluster_num]]

        dist_from_start = min([environment.bfs_dist[ind][0] for ind in cluster_list])
        for j in range(1,cluster_num):
            if environment.bfs_dist[cluster_list[j]][0] == dist_from_start:
                cluster_list[j],cluster_list[0] = cluster_list[0],cluster_list[j]
                break

        
        if cluster_num == 1:
            return cluster_list

        best_dist = inf2
        best_cluster_list = []

        for l in itertools.permutations(range(1,cluster_num),cluster_num-1):

            cluster_root = [cluster_list[0]] + [cluster_list[i] for i in l]
            dist = 0
            for i in range(cluster_num):
                dist += self.cluster_dist[cluster_root[i]][cluster_root[i-1]]

            if dist < best_dist:
                best_dist = dist
                best_cluster_list = cluster_root[:]

        return best_cluster_list

  
    def ans_assert(self):

        for ind,(pos,npos) in enumerate(zip(self.ans,self.ans[1:])):
    
            x,y = id_2_xy(pos)
            nx,ny = id_2_xy(npos)
            dx,dy = nx-x,ny-y

            if (dx,dy) not in DIJ:

                assert False,f"{ind} {pos} {x} {y} to {npos} {nx} {ny}"

    def out_ans(self):
        self.ans_assert()
        output = []
        for pos,npos in zip(self.ans,self.ans[1:]):

            x,y = id_2_xy(pos)
            nx,ny = id_2_xy(npos)
            dx,dy = nx-x,ny-y

            output.append(DIR[DIJ.index((dx,dy))])

        print("".join(output))

        exit()


    def get_point_score(self,vis_time,d,T):
    
        if vis_time == []:
            return inf

        base = d*(T-vis_time[-1])
        now = 0
        score = 0
        for t in vis_time:
            dif = t - now
            if dif >= 0:
                score += (dif)*(2*base + (dif-1)*d) // 2
            now = t + 1
            base = d

        dif = T-now
        if dif >= 0:
            score += (dif)*(2*base + (dif-1)*d) // 2

        return score

    def calc_detail_score(self,detail_root):

        T = len(detail_root)-1

        vis_time = [[] for i in range(N2)]

        for t,id in enumerate(detail_root):
            vis_time[id].append(t)

        score_list = []
        score = 0
        for i,(d,vis_t) in enumerate(zip(environment.D,vis_time)):
            # print(d,vis_t)
            assert vis_t != [],f"i = {i} d={d} vis_t = {vis_t}"

            new_score = self.get_point_score(vis_t,d,T)
            score += new_score
            score_list.append(new_score//T)

        return score//T,score_list


    def make_block_root_1loop(self):


        self.block_dist = [inf]*environment.grid_num
        self.block_dist[0] = 0
        self.block_average_pos = []

        q = deque([0])
        while q:
            now = q.popleft()
            for nex,_ in environment.edges_grid[now]:
                if self.block_dist[nex] > self.block_dist[now]+1:
                    self.block_dist[nex] = self.block_dist[now]+1
                    q.append(nex)


        for i in range(environment.grid_num):

            xs,ys = 0,0
            for id in environment.grid_point_list[i]:

                x,y = id_2_xy(id)
                xs += x
                ys += y

            xs //= len(environment.grid_point_list[i])
            ys //= len(environment.grid_point_list[i])


            dist = min(min(N-1-xs,xs)**2,min(N-1-ys,ys)**2)
            self.block_average_pos.append(dist)


        vis_block = [0]*environment.grid_num
        vis_block[0] = 1

        now = 0

        block_roots = [0]
        while True:

            not_visit = []
            for i in range(environment.grid_num):
                if vis_block[i] == 0:
                    not_visit.append(i)
            
            if not_visit == []:
                if now != 0:
                    nex = 0
                else:
                    break

            else:
                nex = not_visit[random.randint(0,len(not_visit)-1)]

            ### dp 未訪問を多く使う最短経路 重いblockを優先する

            dp = [inf2 for i in range(environment.grid_num)]
            dp[now] = 0

            h = [[0,now]]
            par = [-1]*environment.grid_num

            while h:
                dis,v = heappop(h)

                if dp[v] != dis:
                    continue

                for nv,_ in environment.edges_grid[v]:
                    nw = self.grid_info[nv][3]
                    ntv = vis_block[nv] ^ 1

                    nd = dis + inf//(1+ntv) - nw
                    if dp[nv] > nd:
                        dp[nv] = nd
                        heappush(h,[nd,nv])
                        par[nv] = v
            


            if not_visit:
                dist_min = [inf2,inf2,inf2]
                nex = -1
                for v in not_visit:
                    ndist = [-self.block_dist[v],self.block_average_pos[v],dp[v]]
                    ndist = [dp[v],-self.block_dist[v],self.block_average_pos[v]]
                    # ndist = [dp[v]//1000,self.block_average_pos[v],-self.block_dist[v]]
                    ndist = [dp[v]//1000,-self.block_dist[v],self.block_average_pos[v]]



                    if dist_min > ndist:
                        nex = v
                        dist_min = ndist

            v = nex

            temp_root = []
            while v != now:
                temp_root.append(v)
                v = par[v]
            
            for block in temp_root[::-1]:
                block_roots.append(block)
                vis_block[block] = 1

            now = nex

        return block_roots

    def make_detail_root(self,block_roots):
    

        pid = 0

        ans = [0]

        vis_time = [0]*N2
        dis_time = [inf]*N2

        visited = [0]*environment.grid_num
        for i in range(len(block_roots)):

            block = block_roots[i]
            assert environment.grid_indexes[pid] == block

            for id in environment.grid_point_list[block]:
                dis_time[id] = inf
                vis_time[id] = 0

            target_list = []
            if i == len(block_roots)-1:
                target_list = [0]

            else:
                nblock = block_roots[i+1]
                for id in environment.grid_point_list[block]:
                    for nid,_ in environment.edges_point[id]:
                        if environment.grid_indexes[nid] == nblock:
                            target_list.append(id)

            
            # print(target_list,i)
            assert target_list

            q = deque()
            for id in target_list:
                dis_time[id] = 0
                q.append(id)

            while q:
                id = q.popleft()
                for nid,_ in environment.edges_point[id]:

                    if environment.grid_indexes[nid] == block and dis_time[nid] > dis_time[id]+1:
                        q.append(nid)
                        dis_time[nid] = dis_time[id] + 1
            
            vis_time[pid] = 1
            if visited[block]:

                for id in environment.grid_point_list[block]:
                    if environment.D[id] <= 500:
                        vis_time[id] = 1


            visited[block] = 1
 
            while True:
                nex_dist = -1
                nex_pos = -1
                for nid,_ in environment.edges_point[pid]:
                    if environment.grid_indexes[nid] == block and vis_time[nid] == 0:
                        if nex_dist < dis_time[nid]:
                            nex_dist = dis_time[nid]
                            nex_pos = nid

                
                if nex_dist != -1:

                    nid = nex_pos

                    ans.append(nid)
                    pid = nid
                    vis_time[pid] = 1

                    continue

                dis_dic = {}
                par_dic = {}
                for id in environment.grid_point_list[block]:
                    dis_dic[id] = inf
                dis_dic[pid] = 0

                q = deque([pid])

                nex_pos = -1
                while q:
                    id = q.popleft()
                    d = dis_dic[id]
                    if vis_time[id] == 0:
                        nex_pos = id
                        break

                    for nid,_ in environment.edges_point[id]:

                        if environment.grid_indexes[nid] == block and dis_dic[nid] > d+1:
                            q.append(nid)
                            dis_dic[nid] = d+1
                            par_dic[nid] = id
                    


                if nex_pos != -1:

                    nid = nex_pos

                    moves = []
                    while nid != pid:
                        moves.append(nid)
                        nid = par_dic[nid]

                    for mv in moves[::-1]:
                        ans.append(mv)
                        pid = mv

    
                    vis_time[pid] = 1  
                    continue

                nex_dist = inf
                nex_pos = -1

                for key,value in dis_dic.items():
                    if key not in target_list:
                        continue
                    if value < nex_dist:
                        nex_dist = value
                        nex_pos = key


                assert nex_pos != -1

                nid = nex_pos
                moves = []
                while nid != pid:
                    moves.append(nid)
                    nid = par_dic[nid]

                for mv in moves[::-1]:
                    ans.append(mv)
                    pid = mv


                if i == len(block_roots) -1:
                    assert pid == 0
                    break

                for nid,_ in environment.edges_point[pid]:
                    if environment.grid_indexes[nid] == nblock:
                        ans.append(nid)
                        pid = nid
                        break
                break

        return ans

    
    def make_cluster_grid_root(self,now,now_list,nex_list):

        if nex_list == []:
            return [],now

        if now_list == []:
            
            dist = inf
            cand = -1
            for nex in nex_list:
                if environment.grid_dist[now][nex] < dist:
                    dist = environment.grid_dist[now][nex]
                    cand = nex

            
            return [],cand

        # print("here",now,now_list,nex_list)
        assert now in now_list

        grid_root = []
        dist = inf
        now_cand = -1
        nex_cand = -1
        for now_ind in now_list:
            for nex_ind in nex_list:
                if dist > environment.grid_dist[now_ind][nex_ind]:
                    dist = environment.grid_dist[now_ind][nex_ind]
                    now_cand = now_ind
                    nex_cand = nex_ind

            
        vis_count = {}
        for now_ind in now_list:
            vis_count[now_ind] = 0
        # print(vis_count,now_cand,nex_cand)
        grid_root.append(now)
        vis_count[now] = 1
        while True:

            cand = -1
            dist = -1
            for nex,_ in environment.edges_grid[now]:
                if nex in vis_count and vis_count[nex] == 0:
                    if dist < environment.grid_dist[now_cand][nex]:
                        dist = environment.grid_dist[now_cand][nex]
                        cand = nex


            
            if cand != -1:
                vis_count[cand] = 1
                now = cand
                grid_root.append(now)

                continue

            dist = inf
            for nex in vis_count.keys():
                if vis_count[nex]:
                    continue
                if dist > environment.grid_dist[now][nex]:
                    dist = environment.grid_dist[now][nex]
                    cand = nex

            
            if cand != -1:
                vis_count[cand] = 1
                now = cand
                grid_root.append(now)
                continue

            
            if now != now_cand:
                grid_root.append(now_cand)
            
            # grid_root.append(nex_cand)
            now = nex_cand
            break
        
        # print(grid_root,now)
        return grid_root,now

      
    def make_cluster_grid_full_root(self,cluster_list,grid_group_indexes,grid_visit_pos):

        
        now = 0

        grid_root = []
        grid_root2 = []

        find = 0

        if find == 0:
            new_root,now = self.make_cluster_grid_root(now,[0],self.cluster_grid_list[cluster_list[0]])

        
        for grid_group in grid_group_indexes:
            if grid_group == []:
                continue
            # print(grid_group,now)
            visit_list = [[] for i in range(len(cluster_list)*2)]


            for gid in grid_group:
                visit_list[grid_visit_pos[gid]*2-1].append(gid)

            
            for i,cid in enumerate(cluster_list):
                for gid in self.cluster_grid_list[cid]:
                    visit_list[i*2].append(gid)

            visit_list_new = []
            for v in visit_list:
                if v:
                    visit_list_new.append(v)

            visit_list = visit_list_new
            loop_size = len(visit_list)

            for i in range(loop_size):
                grid_root2.append(visit_list[i])
                # print(visit_list[i],"i = ",i)
                new_root,now = self.make_cluster_grid_root(now,visit_list[i],visit_list[(i+1)%loop_size])
                if new_root != []:
                    
                    if len(new_root) > 1 and new_root[0] == new_root[-1]:
                        new_root = new_root[1:]
                    grid_root.append(new_root)

        if grid_root[-1][-1] != 0:
            grid_root.append([0])
            grid_root2.append([0])

        return grid_root,grid_root2


    def make_cluster_detail_root(self,block_roots):
        

        pid = 0

        ans = [0]

        vis_time = [-1]*N2
        dis_time = [inf]*N2

        visited = [0]*environment.grid_num
        # print(block_roots)
        ans_size = 1
        vis_time[0] = 0
        # print("Here2")
        # print(block_roots)
        step_sizes = []
        for i in range(len(block_roots)):
            
            block_root = block_roots[i]

            # print(block_root)
            for bid,block in enumerate(block_root):
                move_path = environment.get_shortest_root(pid,block)

                for mv in move_path:
                    ans.append(mv)
                    vis_time[mv] = ans_size
                    ans_size += 1
                if move_path:
                    pid = move_path[-1]

                # print(block_root,environment.grid_point_list[block])
                assert environment.grid_indexes[pid] == block

                for id in environment.grid_point_list[block]:
                    dis_time[id] = inf

                target_list = []
                if i == len(block_roots)-1 and bid == len(block_root)-1:
                    target_list = [0]

                else:
                    if bid == len(block_root)-1:
                        nblock = block_roots[i+1][0]
                    else:
                        nblock = block_root[bid+1]


                    mi = inf

                    for id in environment.grid_point_list[block]:
                        mi = min(mi,environment.bfs_dist[nblock][id])

                    for id in environment.grid_point_list[block]:

                        if mi == environment.bfs_dist[nblock][id]:
                            target_list.append(id)

                vis_time[pid] = ans_size
                if i == len(block_roots)-1 and bid == len(block_root)-1 and visited[block]:

                    assert block == 0

                    # for id in environment.grid_point_list[block]:
                    #     vis_time[id] = 1



                if visited[block]:

                    for id in environment.grid_point_list[block]:
                        if id == pid:
                            continue
                        w = self.score_list[id]/self.score_avg
                        # if w >= 2:
                        #     vis_time[id] = -1
                        if w >= 3:
                            vis_time[id] = -1
                        elif 2 <= w < 3 and random.random() < 0.5:
                            vis_time[id] = -1
                        
                        elif (ans_size-vis_time[id])*environment.D[id]/2 >= self.score_avg:
                            vis_time[id] = -1
                        # if w  < 2:
                        #     vis_time[id] = 1
                        # elif w < 3 and random.random() < 0.5:
                        #     vis_time[id] = 1

                        # if environment.D[id]/environment.D_avg < 3:
                        #     vis_time[id] = 1
                visited[block] = 1
                while True:
                    nex_dist = -1
                    nex_pos = -1
                    for nid,_ in environment.edges_point[pid]:

                        if environment.grid_indexes[nid] == block and vis_time[nid] == -1:
                            if nex_dist < environment.bfs_dist[nblock][nid]:
                                nex_dist = environment.bfs_dist[nblock][nid]
                                nex_pos = nid
                    if nex_dist != -1:

                        ans.append(nex_pos)
                        pid = nex_pos
                        vis_time[pid] = ans_size
                        assert vis_time[pid] != -1
                        ans_size += 1

                        continue
                    dis_dic = {}
                    par_dic = {}
                    for id in environment.grid_point_list[block]:
                        dis_dic[id] = inf
                    dis_dic[pid] = 0
                    q = deque([pid])

                    nex_pos = -1
                    while q:
                        id = q.popleft()
                        d = dis_dic[id]
                        if vis_time[id] == -1:
                            nex_pos = id
                            break

                        for nid,_ in environment.edges_point[id]:
                            if environment.grid_indexes[nid] == block and dis_dic[nid] > d+1:
                                q.append(nid)
                                dis_dic[nid] = d+1
                                par_dic[nid] = id
                    
                    if nex_pos != -1:
                        nid = nex_pos

                        moves = []
                        while nid != pid:
                            moves.append(nid)
                            nid = par_dic[nid]

                        for mv in moves[::-1]:
                            ans.append(mv)
                            vis_time[mv] = ans_size
                            
                            ans_size += 1
                            pid = mv

                        # vis_time[pid] = 1  
                        assert vis_time[pid] != -1
                        continue

                    nex_dist = inf
                    nex_pos = -1

                    for key,value in dis_dic.items():
                        if key not in target_list:
                            continue
                        if value < nex_dist:
                            nex_dist = value
                            nex_pos = key

                    assert nex_pos != -1

                    nid = nex_pos
                    moves = []
                    while nid != pid:
                        moves.append(nid)
                        nid = par_dic[nid]

                    for mv in moves[::-1]:
                        ans.append(mv)
                        vis_time[mv] = ans_size
                        ans_size += 1
                        pid = mv

                    # vis_time[pid] = 1  
                        
                    if i == len(block_roots)-1 and bid == len(block_root)-1:
                        assert pid == 0
                        break

                    break
            step_sizes.append(ans_size)

        assert sum(visited) == environment.grid_num
        return ans,step_sizes


    def make_cluster_detail_root_2(self,block_roots):
      
        pid = 0

        ans = [0]

        vis_time = [-1]*N2
        dis_dic = [-1]*N2
        par_dic = [-1]*N2
        block_point_info = [-1]*N2

        step_sizes = []
        visited = [0]*environment.grid_num
        # print(block_roots)
        ans_size = 1
        vis_time[0] = 0

        for i in range(len(block_roots)):
            
            block_root = block_roots[i]
            move_path = environment.get_shortest_root_blocks(pid,block_root)
            for mv in move_path:
                ans.append(mv)
                vis_time[mv] = ans_size
                ans_size += 1
            if move_path:
                pid = move_path[-1]
            

            block_indexes = []

            for block in block_root:
                for id in environment.grid_point_list[block]:
                    block_indexes.append(id)
                    block_point_info[id] = i

            assert block_point_info[id] == i

            target_list = []
            nblock_indexes = []
            if i == len(block_roots)-1:
                nblock_indexes.append(0)

            else:
                nblocks = block_roots[i+1]

                for nblock in nblocks:
                    for id in environment.grid_point_list[nblock]:
                        nblock_indexes.append(id)

            
            nblock_bfs_dist,nblock_dijkstra_dist = environment.calc_shortest_root(nblock_indexes)

            mi = inf

            for id in block_indexes:

                mi = min(mi,nblock_bfs_dist[id])

            for id in block_indexes:
                if mi == nblock_bfs_dist[id]:
                    target_list.append(id)
            
            assert target_list
            vis_time[pid] = ans_size

            for id in block_indexes:
                if id == pid:
                    continue
                w = self.score_list[id]/self.score_avg

                if w >= 3:
                    vis_time[id] = -1
                elif 2 <= w < 3 and random.random() < 0.5:
                    vis_time[id] = -1
                
                elif (ans_size-vis_time[id])*environment.D[id]/2 >= self.score_avg:
                    vis_time[id] = -1
  
            while True:
                nex_dist = -1
                nex_pos = -1
                for nid,_ in environment.edges_point[pid]:

                    if block_point_info[nid] == i and vis_time[nid] == -1:
                        ndist = [nblock_bfs_dist[nid],]
                        if nex_dist < nblock_bfs_dist[nid]:
                            nex_dist = nblock_bfs_dist[nid]
                            nex_pos = nid
                if nex_dist != -1:

                    ans.append(nex_pos)
                    pid = nex_pos
                    vis_time[pid] = ans_size
                    assert vis_time[pid] != -1
                    ans_size += 1
                    continue
                
                # print("A")
                
                for id in block_indexes:
                    dis_dic[id] = inf

                dis_dic[pid] = 0
                q = deque([pid])
                # h = [[0,pid]]

                nex_pos = -1
                while q:
                    id = q.popleft()
                    d = dis_dic[id]
                    if vis_time[id] == -1:
                        nex_pos = id
                        break

                    for nid,_ in environment.edges_point[id]:
                        if block_point_info[nid] == i and dis_dic[nid] > d+1:
                            q.append(nid)
                            dis_dic[nid] = d+1
                            par_dic[nid] = id
                
                if nex_pos != -1:
                    nid = nex_pos

                    moves = []
                    while nid != pid:
                        moves.append(nid)
                        nid = par_dic[nid]

                    for mv in moves[::-1]:
                        ans.append(mv)
                        vis_time[mv] = ans_size
                        
                        ans_size += 1
                        pid = mv

                    # vis_time[pid] = 1  
                    assert vis_time[pid] != -1
                    continue

                nex_dist = inf
                nex_pos = -1

                for id in block_indexes:
                    if vis_time[id] != -1:
                        continue

                    dis = environment.bfs_dist[environment.grid_indexes[id]][pid]
                    if dis < nex_dist:
                        nex_dist = dis
                        nex_pos = id

                
                if nex_pos != -1:
                    nid = nex_pos

                    moves = environment.get_shortest_root_point(pid,nex_pos)
                    for mv in moves:
                        ans.append(mv)
                        vis_time[mv] = ans_size
                        
                        ans_size += 1
                        pid = mv
                    assert pid == nex_pos
                    # vis_time[pid] = 1  
                    assert vis_time[pid] != -1
                    continue

                root = []
                for key in target_list:
                    moves = environment.get_shortest_root_point(pid,key)
                    value = len(moves)

                    if value < nex_dist:
                        nex_dist = value
                        nex_pos = key
                        root = moves

                assert nex_pos != -1

               
                for mv in root:
                    ans.append(mv)
                    vis_time[mv] = ans_size
                    ans_size += 1
                    pid = mv

                    assert vis_time[pid] != -1

                # vis_time[pid] = 1  
                    
                if i == len(block_roots)-1:
                    assert pid == 0
                    break

                break

            step_sizes.append(ans_size)

        # assert sum(visited) == environment.grid_num
        return ans,step_sizes


    def group_separate_optimize(self,grid_group_indexes,grid_cost,grid_dist):


        new_grid_group_indexes:list = []
        new_grid_cost = []
        new_grid_pos = [-1]*environment.grid_num
        size = 0
        h = []
        for i,g in enumerate(grid_group_indexes):
            if g:
                new_grid_group_indexes.append(g[:])
                new_grid_cost.append(grid_cost[i]+grid_dist[i])
                for ind in g:
                    new_grid_pos[ind] = size
                heappush(h,[new_grid_cost[-1],size])
                size += 1
        for _ in range(1000):

            rind = random.randint(0,size-1)

            rind2 = random.randint(0,len(new_grid_group_indexes[rind])-1)

            now = new_grid_group_indexes[rind][rind2]
            
            grid_size = environment.grid_info[now][1]
            cand = -1
            best = -1

            if len(new_grid_group_indexes[rind]) == 1:
                continue
            for nex,_ in environment.edges_grid[now]:
                nind = new_grid_pos[nex]
                if nind == rind:
                    continue
                    
                if nind != -1:
                    cost = new_grid_cost[rind]**2 + new_grid_cost[nind]**2
                    cost -= (new_grid_cost[rind]-grid_size//2)**2 + (new_grid_cost[nind]+grid_size)**2

                    if best < cost:
                        best = cost
                        cand = nind

                else:
                    c,nind = -1,-1
                    while h:
                        c,nind = heappop(h)
                        if new_grid_cost[nind] != c:
                            continue
                        break

                    if nind == -1:
                        continue

                    if nind == rind:
                        heappush(h,[c,nind])
                        continue

                    cost = new_grid_cost[rind]**2 + new_grid_cost[nind]**2
                    cost -= (new_grid_cost[rind]-grid_size//2)**2 + (new_grid_cost[nind]+grid_size)**2

                    if best < cost:
                        best = cost
                        cand = nind

            
            if cand == -1:
                continue

            new_grid_cost[rind] -= grid_size//2
            new_grid_cost[cand] += grid_size

            # assert new_grid_cost[rind] >= 0
            new_grid_group_indexes[rind].remove(now)
            new_grid_pos[now] = cand
            new_grid_group_indexes[cand].append(now)

            # assert new_grid_group_indexes[rind]
            heappush(h,[new_grid_cost[rind],rind])
            heappush(h,[new_grid_cost[cand],cand])

            # print("best",best,new_grid_group_indexes[rind],new_grid_group_indexes[cand])

                

        # print(new_grid_cost,base)   

        
    


        return new_grid_group_indexes


    def make_cluster_root(self,cluster_list,cluster_num):

        grid_dist_to_cluster = [[inf]*cluster_num for i in range(environment.grid_num)]
        grid_visit_pos = [-1]*environment.grid_num

        for i,gid in enumerate(environment.grid_indexes):

            for j,p in enumerate(cluster_list):
                grid_dist_to_cluster[gid][j] = min(grid_dist_to_cluster[gid][j],self.bfs_dist[p][i])

        
        grid_cost = [0]*environment.grid_num
        grid_dist = [0]*environment.grid_num
        grid_leader = [-1]*environment.grid_num

        is_use_group = [1]*environment.grid_num

        for p in cluster_list:
            for gid in self.cluster_grid_list[p]:
                is_use_group[gid] = 0
        
        h = []
        for i in range(environment.grid_num):
            if is_use_group[i] == 0:
                continue
            grid_cost[i] = self.grid_info[i][1]
            dist = inf
            vis_time = -1
            for j in range(cluster_num):
                if dist > grid_dist_to_cluster[i][j]+grid_dist_to_cluster[i][j-1]:
                    dist = grid_dist_to_cluster[i][j]+grid_dist_to_cluster[i][j-1]
                    vis_time = j

            grid_dist[i] = dist
            grid_visit_pos[i] = vis_time


            heappush(h,[grid_cost[i]+grid_dist[i],i])

        # print(h)
        grid_group_indexes = [[] for i in range(environment.grid_num)]
        for i in range(environment.grid_num):
            if is_use_group[i]:
                grid_group_indexes[i].append(i)
                grid_leader[i] = i

        best_score = inf2
        best_ans = []
        best_cand_root = []
        best_cand_root2 = []
        best_chose = ""
        best_score_list = []
        best_step_size = []
        loop_num = sum(is_use_group)

        while len(h) >= 2:
            c,ind = heappop(h)
            if grid_cost[ind] + grid_dist[ind] != c:
                continue
            
            if loop_num <= 8:
                new_grid_group_indexes = self.group_separate_optimize(grid_group_indexes,grid_cost,grid_dist)
                cand_root,cand_root2 = self.make_cluster_grid_full_root(cluster_list,new_grid_group_indexes,grid_visit_pos)

                detail_root,step_size = self.make_cluster_detail_root(cand_root)
                score,score_list = self.calc_detail_score(detail_root)
            
                if score < best_score:
                    best_score = score
                    best_ans = detail_root[:]
                    best_cand_root = cand_root[:]
                    best_score_list = score_list
                    best_cand_root2 = cand_root2
                    best_step_size = step_size
                    best_chose = f"cluster num = {cluster_num} loop size = {loop_num+1} group adjusted"

                cand_root,cand_root2 = self.make_cluster_grid_full_root(cluster_list,grid_group_indexes,grid_visit_pos)
                # print("Here3")
                # print(cand_root)
                detail_root,step_size = self.make_cluster_detail_root(cand_root)
                score,score_list = self.calc_detail_score(detail_root)

                if score < best_score:
                    best_score = score
                    best_ans = detail_root[:]
                    best_cand_root = cand_root[:]
                    best_score_list = score_list
                    best_cand_root2 = cand_root2
                    best_step_size = step_size
                    best_chose = f"cluster num = {cluster_num} loop size = {loop_num+1}"
                temp = h[:] + [[c,ind]]
                # print(f"cluster num = {cluster_num} loop num = {loop_num} score = {score}",temp)
            loop_num -= 1
            merge_cand = set()

            for id in grid_group_indexes[ind]:

                for nid,_ in environment.edges_grid[id]:
                    if grid_leader[nid] != ind and is_use_group[nid]:
                        merge_cand.add(grid_leader[nid])


            if merge_cand:
                cand = -1
                min_cost = inf
                for nid in merge_cand:
                    ncost = grid_cost[nid]+grid_dist[nid]
                    if min_cost > ncost:
                        min_cost = ncost
                        cand = nid

                for id in grid_group_indexes[ind]:
                    grid_group_indexes[cand].append(id)
                    grid_leader[id] = cand
                
                grid_group_indexes[ind] = []

                grid_cost[cand] += grid_cost[ind]

                for j in range(cluster_num):
                    grid_dist_to_cluster[cand][j] = min(grid_dist_to_cluster[cand][j],grid_dist_to_cluster[ind][j])

                dist = inf
                for j in range(cluster_num):
                    dist = min(dist,grid_dist_to_cluster[cand][j]+grid_dist_to_cluster[cand][j-1])
                grid_dist[cand] = dist

                heappush(h,[grid_cost[cand]+grid_dist[cand],cand])

            else:
                cand = -1
                while h:
                    nc,nind = heappop(h)
                    if grid_dist[nind]+grid_cost[nind] != nc or nind == ind:
                        continue
                    else:
                        cand = nind
                        break
                if cand == -1:
                    break

                assert ind != cand

                for id in grid_group_indexes[ind]:
                    grid_group_indexes[cand].append(id)
                    grid_leader[id] = cand
                
                grid_group_indexes[ind] = []

                grid_cost[cand] += grid_cost[ind]
                heappush(h,[grid_cost[cand]+grid_dist[cand],cand])

        return best_score,best_ans,best_cand_root,best_chose,best_score_list,best_cand_root2,best_step_size



    def optimize(self,cand_root,cluster_info,best_score_list):

        T = 0
  
        last = 0
        vis_time = [[] for i in range(environment.grid_num)]


        next_list = [-1]*len(cand_root)
        last_list = [-1]*len(cand_root)
        last_list[0] = 0
        for i,root in enumerate(cand_root):
            if i:
                next_list[i-1] = root[0]
            if i < len(cand_root)-1:
                last_list[i+1] = root[-1]


            for ind in root:
                T += environment.grid_dist[last][ind]
                last = ind
                vis_time[ind].append(T)
                T += environment.grid_info[ind][1]
        
        T += environment.grid_dist[0][last]


        grid_scores = [[0,i] for i in range(environment.grid_num)]
        for i,s in enumerate(best_score_list):
            grid_scores[environment.grid_indexes[i]][0] += s

        grid_scores.sort(reverse=True)


        turn_avg = sum(best_score_list)


        score = 0
        score_list = []
        for ind in range(environment.grid_num):

            count = self.get_point_score(vis_time[ind],environment.grid_info[ind][2],T)
            score_list.append(count)
            score += count

        
        now = 0
        while time.time() - stime < 1.5:


            _,ind = grid_scores[now]


            cand = []

            best = 0
            s = environment.grid_info[ind][1]
            pos = 0
            last = 0
            d = environment.grid_info[ind][2]
            for i,root in enumerate(cand_root):

                if last_list[i] != -1:

                    t = s + environment.grid_dist[ind][last_list[i]] + environment.grid_dist[ind][root[0]]


                    temp = t * turn_avg

                    temp_vis_time = vis_time[ind][:]
                    temp_vis_time.append(pos+t)

                    temp_vis_time.sort()
                    count = self.get_point_score(temp_vis_time,d,T)

                    temp += count - score_list[ind]
                    print(temp)
                    if temp < best:
                        best = temp
                        cand = [t,temp_vis_time,count,i,0]


                for j,(ind1,ind2) in enumerate(zip(root,root[1:])):
                    pos += environment.grid_dist[last][ind1]
                    pos += environment.grid_info[ind1][1]

                    last = ind1


                    t = s + environment.grid_dist[ind][last] + environment.grid_dist[ind][ind2]


                    temp = t * turn_avg

                    temp_vis_time = vis_time[ind][:]
                    temp_vis_time.append(pos+t)

                    temp_vis_time.sort()
                    count = self.get_point_score(temp_vis_time,d,T)

                    temp += count - score_list[ind]
                    print(temp)
                    if temp < best:
                        best = temp
                        cand = [t,temp_vis_time,count,i,j+1]

                ind2 = root[-1]
                pos += environment.grid_dist[last][ind2]
                pos += environment.grid_info[last][1]

                if next_list[i] != -1:
                    t = s + environment.grid_dist[ind][next_list[i]] + environment.grid_dist[ind][root[-1]]


                    temp = t * turn_avg

                    temp_vis_time = vis_time[ind][:]
                    temp_vis_time.append(pos+t)

                    temp_vis_time.sort()
                    count = self.get_point_score(temp_vis_time,d,T)

                    temp += count - score_list[ind]
                    print(temp)
                    if temp < best:
                        best = temp
                        cand = [t,temp_vis_time,count,i,len(root)]

            print(now,best,cand)

            if best < 0:

                t,temp_vis_time,count,ins,pos = cand
                T += t
                vis_time[ind] = temp_vis_time
                score_list[ind] = count
                cand_root[ins].insert(pos,ind)


        return cand_root


            



            
        

    def solve(self):
        

        best_cand_root = self.make_block_root_1loop()
        best_ans = self.make_detail_root(best_cand_root)
        best_score,best_score_list = self.calc_detail_score(best_ans)
        
        best_chose = "cluster num = 0 loop size = 1"
        best_cand_root2 = [[i for i in range(environment.grid_num)]]
        best_step_size = []
        self.score_list = best_score_list
        self.score_avg = best_score//N2
        best_cluster = []
        self._build_cluster_info2()

        cluster_info = [0]*environment.grid_num

        for cluster_num in range(1,min(5,self.cluster_num)+1):

            cluster_group = self.make_cluster_group(cluster_num)
            
            cluster_score,cluster_root,cand_root,cand_chose,cand_score_list,cand_root2,cand_step_size = self.make_cluster_root(cluster_group,cluster_num)
            if cluster_score < best_score:
                best_cluster = cluster_group
                best_score = cluster_score
                best_ans = cluster_root
                best_cand_root = cand_root
                best_chose = cand_chose
                best_score_list = cand_score_list
                best_cand_root2 = cand_root2
                best_step_size = cand_step_size
        self.score_list = best_score_list
        self.score_avg = best_score//N2

        self._build_cluster_info2()
        for cluster_num in range(1,min(5,self.cluster_num)+1):
    
            cluster_group = self.make_cluster_group(cluster_num)
            cluster_score,cluster_root,cand_root,cand_chose,cand_score_list,cand_root2,cand_step_size = self.make_cluster_root(cluster_group,cluster_num)
            if cluster_score < best_score:
                best_cluster = cluster_group
                best_score = cluster_score
                best_ans = cluster_root
                best_cand_root = cand_root
                best_chose = cand_chose
                best_score_list = cand_score_list
                best_cand_root2 = cand_root2
                best_step_size = cand_step_size

        cand_root,cand_step_size = self.make_cluster_detail_root_2(best_cand_root2)

        score,score_list = self.calc_detail_score(cand_root)
        if score < best_score:
            best_score = score
            best_ans = cand_root
            best_cand_root = []
            best_chose = best_chose + " adjust loot"
            best_score_list = score_list
            best_step_size = cand_step_size

        print(best_cand_root)
        print(best_score)

        for i,cid in enumerate(best_cluster):
            for gid in self.cluster_grid_list[cid]:
                cluster_info[gid] = 1

        # cand_root = self.optimize(best_cand_root,cluster_info,best_score_list)
        # detail_root,step_size = self.make_cluster_detail_root(cand_root)
        # score,score_list = self.calc_detail_score(detail_root)

        # if score < best_score:
        #     self.ans = detail_root

        # for s1,s2 in zip(best_step_size,best_step_size[1:]):
        #     print(s2-s1)
        # print(best_step_size)
        self.ans = best_ans
        
        # print(best_chose)
        self.out_ans()



solver = Solver()
solver.solve()
