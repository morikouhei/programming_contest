import time
import sys
from collections import deque

stime = time.time()
TIME_LIM = 2
inf = 1<<10

class Judge:


    def __init__(self,blocks,package_num):

        self.blocks = blocks
        self.DEBUG = 0
        self.TD = []
        self.package_num = package_num
        self.ind = -1
    def get_TD(self):
        if self.DEBUG:
            self.TD = [int(input()) for i in range(self.package_num)]

    def pass_TD(self):
        self.ind += 1
        assert self.ind < self.package_num

        if self.DEBUG:
            print(f"# pass id = {self.TD[self.ind]}")
            return self.TD[self.ind]
        else:
            td = int(input())
            return td
       

    
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
 
    def build(self, list):
        self.tree[1:] = list.copy()
        for i in range(self.size+1):
            j = i + (i & (-i))
            if j < self.size+1:
                self.tree[j] += self.tree[i]

    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s
    # 0 index を 1 index に変更  転倒数を求めるなら1を足していく
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # 総和がx以上になる位置のindex をbinary search
    def bsearch(self,x):
        le = 0
        ri = 1<<(self.size.bit_length()-1)
        while ri > 0:
            if le+ri <= self.size and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri >>= 1
        return le+1

D,N = map(int,input().split())


CX,CY = 0,D//2
blocks = [[0]*D for i in range(D)]
for i in range(N):
    x,y = map(int,input().split())
    blocks[x][y] = 2
package = D**2-1-N
ans = [[-1]*D for i in range(D)]
judge = Judge(blocks,package)
judge.get_TD()
bit = BIT(D**2+1)
bit_after = BIT(D**2+1)
for i in range(package):
    bit_after.add(i,1)

puts_package = 0
def get_inversion_sum(x):
    return puts_package - bit.sum(x) 

def get_inversion_sum_after(x):
    return bit_after.sum(D**2) - bit_after.sum(x+1)

def out(x,y):
    print(x,y)
    sys.stdout.flush()


def bfs(x=-1,y=-1):

    dist = [[inf]*D for i in range(D)]

    if x != -1:
        assert blocks[x][y] == 0
        blocks[x][y] = 1

    dist[0][D//2] = 0
    q = deque([[0,D//2]])


    while q:
        nx,ny = q.popleft()

        for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            nnx,nny = nx+dx,ny+dy
            if 0 <= nnx < D and 0 <= nny < D and blocks[nnx][nny] == 0:
                if dist[nnx][nny] > dist[nx][ny] + 1:
                    q.append([nnx,nny])
                    dist[nnx][nny] = dist[nx][ny] + 1

    if x != -1:
        blocks[x][y] = 0

    return dist

for _ in range(package):

    id = judge.pass_TD()

    inversion_num = get_inversion_sum_after(id)

    base_dist = bfs()

    dif_min = inf
    cand_x,cand_y = -1,-1
    for i in range(D):
        for j in range(D):
            if blocks[i][j]:
                continue

            if (i,j) == (CX,CY):
                continue


            dist = bfs(i,j)

            dis_base = base_dist[i][j]
            dif_id = 0

            for x in range(D):
                for y in range(D):
                    if blocks[x][y] or (x,y) == (i,j):
                        continue
                    if dist[x][y] == inf:
                        dif_id = inf<<10
                    if dist[x][y] < dis_base:
                        dif_id -= 1
                    else:
                        dif_id += 1
            
            dif_id = abs(dif_id)
            if dif_id < dif_min:
                dif_min = dif_id
                cand_x,cand_y = i,j

    

                    
    assert cand_x != -1
    ans[cand_x][cand_y] = id

    out(cand_x,cand_y)
    blocks[cand_x][cand_y] = 1

    bit.add(id,1)
    bit_after.add(id,-1)
    puts_package += 1


dist = [[inf]*D for i in range(D)]
dist[CX][CY] = 0

bit = BIT(D**2+1)
next_list = []

for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
    nx = CX+dx
    ny = CY+dy
    if 0 <= nx < D and 0 <= ny < D and ans[nx][ny] != -1 and dist[nx][ny] > dist[CX][CY]+1:
        next_list.append([ans[nx][ny],nx,ny])
        dist[nx][ny] = 1
        ans[nx][ny] = -1



for _ in range(package):

    best_id = -1
    best_num = inf
    for ind,(id,x,y) in enumerate(next_list):

        inversion_num = id - bit.sum(id)
        if inversion_num < best_num:
            best_num = inversion_num
            best_id = ind

    
    id,x,y = next_list[best_id]
    next_list.pop(best_id)

    for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx < D and 0 <= ny < D and ans[nx][ny] != -1 and dist[nx][ny] > dist[CX][CY]+1:
            next_list.append([ans[nx][ny],nx,ny])
            dist[nx][ny] = dist[x][y] + 1
            ans[nx][ny] = -1

    out(x,y)
    bit.add(id,1)
