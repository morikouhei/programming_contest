import subprocess
import time
import os
import random
import math
import matplotlib.pyplot as plt
import pandas as pd
#コードをコンパイルする(pythonなどの場合不要)

start = time.time()
N = int(input())
print("number test = ",N)

#パソコンのプロセス数
max_process = 5 #要変更
proc_list = []
S_list = [str(i).zfill(4) for i in range(N)]

for i in range(N):
    # S = files[i]

    S = str(i).zfill(4)

    proc = subprocess.Popen(f"python3 /Users/morikouhei/github/programming_contest/atcoder/ahc/ahc027/na.py < in/{S}.txt > out/{S}.txt", shell=True)#要変更
    proc_list.append(proc)
    if (i + 1) % max_process == 0 or (i + 1) == N:
        for subproc in proc_list:
            try:
                subproc.wait(timeout=10)
            except:
                print("stop")
        proc_list = []


print("time: ", time.time() - start)


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


count_dic = {}
def calc_score(input_path,output_path):
 
    with open(input_path) as f:
        lines = f.readlines()
        N = int(lines[0].replace("\n",""))
        H = [list(map(int,lines[i].replace("\n",""))) for i in range(1,N)]
        V = [list(map(int,lines[i].replace("\n",""))) for i in range(N,2*N)]
        D = [list(map(int,lines[i].replace("\n","").split())) for i in range(2*N,3*N)]


    with open(output_path) as f:
        lines = f.readlines()
        
        L = lines[0].replace("\n","")

    T = len(L)


    DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIR = "RDLU"

    history = [[[] for i in range(N)] for j in range(N)]

    x,y = 0,0
    history[x][y].append(0)
    D_sum = 0

    for i in range(T):

        d = L[i]

        dx,dy = DIJ[DIR.index(d)]

        nx,ny = x+dx,y+dy

        if 0 <= nx < N and 0 <= ny < N:
            if (dx == 0 and V[x][min(y,ny)] == 1) or (dy == 0 and H[min(x,nx)][y] == 1):

                print("move cross thet wall")
                return -1

            else:
                x,y = nx,ny
                history[x][y].append(i+1)
        else:
            print("move outside of area")
            return -1


    if (x,y) != (0,0):
        print("Not return to start")
        return -1

    S_sum = 0

    for i in range(N):
        for j in range(N):
            d = D[i][j]
            D_sum += d
            if history[i][j] == []:
                print("Not visit",i,j)
                return -1

            start = T - history[i][j][-1]

            base = d*start

            history[i][j].append(T)

            now = 0
            count = 0
            for t in history[i][j]:

                dif = t - now

                if dif >= 0:

                    count += (dif)*(2*base + (dif-1)*d) // 2
                
                now = t + 1
                base = d
            S_sum += count



    S_bar = S_sum / T
    s = lines[0]
    # if s not in count_dic:
    #     count_dic[s] = 0
    # count_dic[s] += 1
    # print(lines[0])
    # print(int(S_bar))
    # print()
    return int(S_bar),D_sum//N**2,int(S_bar)//N**2,N

                

def get_each_score(input_path,output_path):
    DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIR = "RDLU"

    with open(input_path) as f:
        lines = f.readlines()
        N = int(lines[0].replace("\n",""))
        H = [list(map(int,lines[i].replace("\n",""))) for i in range(1,N)]
        V = [list(map(int,lines[i].replace("\n",""))) for i in range(N,2*N)]
        D = [list(map(int,lines[i].replace("\n","").split())) for i in range(2*N,3*N)]

    N2 = N**2
    D_t = []
    for d in D:
        D_t += d
    
    D = D_t

    def id_2_xy(id):
        return divmod(id,N)

    def xy_2_id(x,y):
        return x*N+y



    edges = [[] for i in range(N**2)]
    for x in range(N):
        for y in range(N):
            id = xy_2_id(x,y)
            for (dx,dy),dS in zip(DIJ,DIR):
                nx,ny = x+dx,y+dy

                if 0 <= nx < N and 0 <= ny < N:
                    if (dx == 0 and V[x][min(y,ny)] == 0) or (dy == 0 and H[min(x,nx)][y] == 0):
                        nid = xy_2_id(nx,ny)
                        edges[id].append([nid,dS])

    
    block_ids = [-1]*(N**2)
    GRID_SIZE = 4
    size = 0
    edges_grid = []
    block_avs = []
    for x in range(N):
        for y in range(N):
            id = xy_2_id(x,y)
            if block_ids[id] != -1:
                continue

            lx = x//GRID_SIZE*GRID_SIZE
            ly = y//GRID_SIZE*GRID_SIZE
            rx = min(N,lx+GRID_SIZE)
            ry = min(N,ly+GRID_SIZE)


            weight = 0
            num = 0
            q = [id]
            block_ids[id] = size

            while q:
                pid = q.pop()
                weight += D[pid]
                num += 1

                for nid,_ in edges[pid]:
                    nx,ny = id_2_xy(nid)
                    if lx <= nx < rx and ly <= ny < ry and block_ids[nid] == -1:
                        block_ids[nid] = size
                        q.append(nid)
            
            edges_grid.append(set())
            block_avs.append(weight//num)
        
            size += 1

    

    block_indexs = [[] for i in range(size)]
    for id in range(N2):

        block_indexs[block_ids[id]].append(id)
        for nid,_ in edges[id]:
            if block_ids[id] != block_ids[nid]:
                edges_grid[block_ids[id]].add((block_ids[nid],""))

    for i in range(size):
        edges_grid[i] = list(edges_grid[i])

    
    
    block_sums = sum(block_avs)
    block_avg = block_sums / size
    count = [0]*4

    for d in block_avs:
        s = d / block_avg
        if s <= 1:
            count[0] += 1
        elif s <= 2:
            count[1] += 1
        elif s <= 3:
            count[2] += 1
        else:
            count[3] += 1


    D_sum = sum(D)

    D_avg = D_sum / N**2

    count = [0]*4
    for d in D:

        s = d/D_avg
        if s <= 1:
            count[0] += 1
        elif s <= 2:
            count[1] += 1
        elif s <= 3:
            count[2] += 1
        else:
            count[3] += 1
    
    count = [int(c/N**2*100) for c in count]

    large_grid = [0]*size
    # for i,d in enumerate(block_avs):
    #     if d / block_avg > 3:
    #         large_grid[block_ids[i]] = 1

    for i,d in enumerate(D):
        if d/D_avg > 3:
            large_grid[block_ids[i]] = 1

    uf = Unionfind(size)
    for i in range(size):
        if large_grid[i] == 0:
            continue

        for ni,_ in edges_grid[i]:
            if large_grid[ni]:
                uf.union(i,ni)

        
    nums = 0
    for i in range(size):
        if large_grid[i] == 1 and uf.find(i) == i:
            nums += 1

        

    return D_avg,count,N**2,nums,size

    with open(output_path) as f:
        lines = f.readlines()
        L = lines[0].replace("\n","")

    T = len(L)


    DIJ = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIR = "RDLU"

    history = [[[] for i in range(N)] for j in range(N)]

    x,y = 0,0
    history[x][y].append(0)
    each_result = []
    for i in range(T):

        d = L[i]

        dx,dy = DIJ[DIR.index(d)]

        nx,ny = x+dx,y+dy

        if 0 <= nx < N and 0 <= ny < N:
            if (dx == 0 and V[x][min(y,ny)] == 1) or (dy == 0 and H[min(x,nx)][y] == 1):

                print("move cross thet wall")
                return -1

            else:
                x,y = nx,ny
                history[x][y].append(i+1)
        else:
            print("move outside of area")
            return -1


    if (x,y) != (0,0):
        print("Not return to start")
        return -1

    S_sum = 0
    for i in range(N):
        for j in range(N):
            d = D[i][j]
            if history[i][j] == []:
                print("Not visit",i,j)
                return -1

            start = T - history[i][j][-1]

            base = d*start

            history[i][j].append(T)

            now = 0
            count = 0
            for t in history[i][j]:

                dif = t - now

                if dif >= 0:

                    count += (dif)*(2*base + (dif-1)*d) // 2
                
                now = t + 1
                base = d
            S_sum += count
            each_result.append([d,count//T])



    S_bar = S_sum / T
    return each_result,int(S_bar)



# fig = plt.figure()

# for i in range(400):
#     S = str(i).zfill(4)

#     input_path = f"in/{S}.txt"
#     output_path = f"out/{S}.txt"
#     score_path = f"score/{S}.txt"
#     # calc_score(input_path,output_path)
#     # each_res,S_bar = get_each_score(input_path,output_path)
#     D_avg,count,N2,nums,size = get_each_score(input_path,output_path)
#     print(S)
#     print(f"D_avg = {int(D_avg)}, count = {count}, N2 = {N2}, cluster blocks = {nums} size = {size}")
#     print()
    
# exit()

#     ax = fig.add_subplot(3,3,i-8)

#     plot_X = []
#     plot_Y = []
#     for x,y in each_res:
#         plot_X.append(x)
#         plot_Y.append(y)
    
#     ax.scatter(plot_X,plot_Y)
#     ax.set_title(S_bar)
# plt.show()






sum_score = 0
log_sum = 0
best_sum_score = 0
scores = []
errors = []
num = 400


plot_X = []
plot_Y = []
plot_X2 = []
for i in range(400):
    S = str(i).zfill(4)
    print(S)
    input_path = f"in/{S}.txt"
    output_path = f"out/{S}.txt"
    score_path = f"score/{S}.txt"
    # calc_score(input_path,output_path)
    try:

        score,d_avg,score_avg,n = calc_score(input_path,output_path)
        sum_score += score_avg
        log_sum += math.log2(score_avg)
        scores.append([score_avg,S])
        plot_X.append(d_avg)
        plot_X2.append(n)
        plot_Y.append(score_avg)
    except:
        score = -1
        print("error",i)
        num -= 1


    with open(score_path,"w") as f:
        f.write(str(score))
        


# lis = []
# for key,value in count_dic.items():
#     lis.append([key,value])

# lis.sort(key=lambda x:x[1])

# for key,value in lis:
#     print(key,value)

print("average =", sum_score / num,sum_score,log_sum/num)
scores.sort()
print(scores[:20])
print(scores[-20:])

fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.scatter(plot_X,plot_Y)

ax = fig.add_subplot(1,2,2)
ax.scatter(plot_X2,plot_Y)

plt.show()