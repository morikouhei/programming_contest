import time
import random
from heapq import heappop,heappush
from collections import deque

random.seed(998244353)
stime = time.time()
TIME_LIM = 2

N = int(input())
N2 = N**2
inf = 10**5
inf2 = 10**10
DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DIR = "RDLU"


def id_2_xy(id):
    return divmod(id,N)

def xy_2_id(x,y):
    return x*N+y


class Environment:

    def __init__(self):
        self.edges = [[] for i in range(N2)]
        self.D = [0]*N2
        self.rootD = [0]*N2

        self._input()

    def _input(self):

        H = [list(map(int,input())) for i in range(N-1)]
        V = [list(map(int,input())) for i in range(N)]
        D = [list(map(int,input().split())) for i in range(N)]

        self.D = [0]*N2

        for x in range(N):
            for y in range(N):
                id = xy_2_id(x,y)
                self.D[id] = D[x][y]
                self.rootD[id] = int(D[x][y]**0.5)

                for dx,dy in DIJ:
                    nx,ny = x+dx,y+dy

                    if 0 <= nx < N and 0 <= ny < N:

                        if (dx == 0 and V[x][min(y,ny)] == 0) or (dy == 0 and H[min(x,nx)][y] == 0):
                            nid = xy_2_id(nx,ny)
                            self.edges[id].append(nid)

        
environment = Environment()

class Solver:

    def __init__(self):
        self.ans = [0]
        self.vis_time = [0]*N2
        self.T = 0
        self.pos = 0
        self.visited_count = 0

      
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




    def solve(self):


        bfs_dist = [inf]*N2
        dijkstra_dist = [0]*N2
        par = [-1]*N2


        while True:

            if self.visited_count == N2 and self.pos == 0:
                break


            bfs_dist = [inf]*N2
            dijkstra_dist = [0]*N2
            par = [-1]*N2

            q = [self.pos]
            bfs_dist[self.pos] = 0

            best_nex = -1
            best_nex_score = -1
            while q:
                nq = []

                for now in q:

                    for nex in environment.edges[now]:
                        if bfs_dist[nex] > bfs_dist[now]+1:
                            bfs_dist[nex] = bfs_dist[now]+1
                            dijkstra_dist[nex] = 0
                            nq.append(nex)

                for now in q:
    
                    for nex in environment.edges[now]:
                        if bfs_dist[nex] != bfs_dist[now]+1:
                            continue

                        ndist = dijkstra_dist[now]+(self.T+bfs_dist[nex]-self.vis_time[nex])*environment.rootD[nex]
                        # print(ndist)
                        if dijkstra_dist[nex] < ndist:
                            dijkstra_dist[nex] = ndist
                            par[nex] = now
                            
                            if best_nex_score < ndist / bfs_dist[nex]:
                                best_nex_score = ndist / bfs_dist[nex]
                                best_nex = nex
                q = nq

 
            if self.visited_count == N2 and self.T > 10**4:
                best_nex = 0
            
            move_root = []
            nex = best_nex
            while nex != self.pos:
                move_root.append(nex)
                nex = par[nex]

            move_root = move_root[::-1]
            if len(move_root) > 5:
                move_root = move_root[:5]

            for pos in move_root:
                self.ans.append(pos)

                self.T += 1
                if self.vis_time[pos] == 0:
                    self.visited_count += 1

                self.vis_time[pos] = self.T
                
                self.pos = pos

            # print(N2-self.visited_count)
            # assert self.pos == best_nex
        self.out_ans()


solver = Solver()
solver.solve()