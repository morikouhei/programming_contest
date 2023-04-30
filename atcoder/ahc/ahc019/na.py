from collections import deque
import time
import random
import copy

TIME_LIM = 6
dirs = [[[0,0,1],[0,0,-1]],[[0,1,0],[0,-1,0]],[[1,0,0],[-1,0,0]]]
dir_list = [[[0,0,1],[0,0,-1]],[[0,1,0],[0,-1,0]],[[1,0,0],[-1,0,0]]]
dir_shuffle_list = dir_list[:]

D = int(input())
xrange = [i for i in range(D)]
yrange = [i for i in range(D)]
zrange = [i for i in range(D)]
f = [[] for i in range(2)]
r = [[] for i in range(2)]
for i in range(2):
    for k in range(D):
        f[i].append(list(map(int,input())))
    for k in range(D):
        r[i].append(list(map(int,input())))

stime = time.time()

invalid_blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]

for i in range(2):
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if f[i][z][x]*r[i][z][y] == 0:
                    invalid_blocks[i][x][y][z] = 1


base_blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]
nmax = 0
def in_pos(x,y,z):
    if 0 <= x < D and 0 <= y < D and 0 <= z < D:
        return 1
    return 0
def calc_score(blocks,nmax):
    used = [0]*nmax
    sizes = [0]*nmax

    for i in range(2):
        use_blocks = [[[0]*D for i in range(D)] for j in range(D)]

        for x in range(D):
            for y in range(D):
                for z in range(D):
                    if use_blocks[x][y][z] or blocks[i][x][y][z] == 0:
                        continue

                    size = 1
                    use_blocks[x][y][z] = 1
                    ind = blocks[i][x][y][z]
                    q = deque([[x,y,z]])

                    while q:
                        nx,ny,nz = q.popleft()
                        for dir in dirs:
                            for dx,dy,dz in dir:
                                nnx,nny,nnz = nx+dx,ny+dy,nz+dz
                                if in_pos(nnx,nny,nnz) == 0:
                                    continue
                                if use_blocks[nnx][nny][nnz]:
                                    continue
                                if blocks[i][nnx][nny][nnz] == ind:
                                    use_blocks[nnx][nny][nnz] = 1
                                    q.append([nnx,nny,nnz])
                                    size += 1

                    sizes[ind-1] = size
                    used[ind-1] += 1


    
    penalty = 0
    for use,size in zip(used,sizes):
        if use == 1:
            penalty += size
        else:
            penalty += 1/size


    return int(10**9*penalty)
def out_ans(nmax,blocks,end):
    ans = [[0 for j in range(D * D * D)] for i in range(2)]
    n = 0
    for i in range(2):
        
        for z in range(D):
            for x in range(D):
                for y in range(D):
                    if blocks[i][x][y][z]:
                        ans[i][x * D * D + y * D + z] = blocks[i][x][y][z]
                        n = max(n,blocks[i][x][y][z])
    
    print(n)
    print(' '.join(map(str, ans[0])))
    print(' '.join(map(str, ans[1])))

    if end:
        exit()

class Output:
    def __init__(self,nmax,blocks):
        self.best_blocks = copy.deepcopy(blocks)
        self.best_nmax = nmax
        self.best_score = calc_score(blocks,nmax)

    def update_best(self,nmax,blocks):
        new_score = calc_score(blocks,nmax)
        if new_score < self.best_score:
            self.best_score = new_score
            self.best_blocks = blocks
            self.best_nmax = nmax

    def update_best_decide(self,nmax,blocks,new_score):
        self.best_score = new_score
        self.best_blocks = blocks
        self.best_nmax = nmax


    def out_ans(self):
        out_ans(self.best_nmax,self.best_blocks,True)

    def out_ans_debug(self):
        out_ans(self.best_nmax,self.best_blocks,False)



nmax = 0
num_blocks = [0,0]
for i in range(2):
    n = 0
    for z in range(D):
        xuse = [0]*D
        yuse = [0]*D
        for x in range(D):
            for y in range(D):
                if f[i][z][x] and r[i][z][y] and (xuse[x]*yuse[y] == 0):
                    n += 1
                    base_blocks[i][x][y][z] = n
                    xuse[x] = 1
                    yuse[y] = 1

    nmax = max(nmax,n)
    num_blocks[i] = n



        
## Todo add block to avoid single point
def add_single_point(blocks,num_blocks,invalid_blocks):

    for i in range(2):
        single_cand = []

        for x in range(D):
            for y in range(D):
                for z in range(D):
                    if blocks[i][x][y][z] == 0:
                        continue

                    nears = 0
                    for dir in dirs:
                        for dx,dy,dz in dir:
                            nx,ny,nz = x+dx,y+dy,z+dz
                            if in_pos(nx,ny,nz) and blocks[i][nx][ny][nz]:
                                nears += 1
                    
                    if nears == 0:
                        single_cand.append([x,y,z])
        
        random.shuffle(single_cand)


        for x,y,z in single_cand:
            nears = 0
            cand = []
            for dir in dirs:
                for dx,dy,dz in dir:
                    nx,ny,nz = x+dx,y+dy,z+dz
                    if in_pos(nx,ny,nz) == 0 or invalid_blocks[i][nx][ny][nz]:
                        continue
                    if blocks[i][nx][ny][nz]:
                        nears += 1
                    else:
                        cand.append([nx,ny,nz])
                    
            if nears or cand == []:
                continue

            rind = random.randint(0,len(cand)-1)
            num_blocks[i] += 1
            nx,ny,nz = cand[rind]
            blocks[i][nx][ny][nz] = 1

    return blocks,num_blocks

## Todo adjust the block num of both 

def add_block(block,num,id,invalid_blocks):
    single_cand = []

    point_list = []
    # print(num)
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if block[x][y][z] == 0:
                    continue

                nears = 0
                for dir in dirs:
                    for dx,dy,dz in dir:
                        nx,ny,nz = x+dx,y+dy,z+dz
                        if in_pos(nx,ny,nz) and block[nx][ny][nz]:
                            nears += 1
                
                point_list.append([x,y,z])
                if nears == 0:
                    single_cand.append([x,y,z])
    
    random.shuffle(single_cand)

    while single_cand and num:
        x,y,z = single_cand.pop()

        nears = 0
        cand = []
        for dir in dirs:
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                if in_pos(nx,ny,nz) == 0 or invalid_blocks[id][nx][ny][nz]:
                    continue
                if block[nx][ny][nz]:
                    nears += 1
                else:
                    cand.append([nx,ny,nz])
                
        if nears or cand == []:
            continue

        rind = random.randint(0,len(cand)-1)
        num -= 1
        nx,ny,nz = cand[rind]
        block[nx][ny][nz] = 1
        point_list.append([nx,ny,nz])
    
    if num == 0:
        return block,1

    while num and point_list:
        rind = random.randint(0,len(point_list)-1)
        x,y,z = point_list[rind]

        cand = []
        for dir in dirs:
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                if in_pos(nx,ny,nz) == 0 or invalid_blocks[id][nx][ny][nz]:
                    continue
                if block[nx][ny][nz] == 0:
                    cand.append([nx,ny,nz])
                
        if cand == []:
            point_list.pop(rind)
            continue


        
        num -= 1
        rind = random.randint(0,len(cand)-1)
        nx,ny,nz = cand[rind]
        block[nx][ny][nz] = 1
        point_list.append([nx,ny,nz])

    if num:
        for x in range(D):
            for y in range(D):
                for z in range(D):
                    if invalid_blocks[id][x][y][z]:
                        continue
                    if block[x][y][z] == 0:
                        block[x][y][z] = 1
                        num -= 1
                    
                    if num == 0:
                        return block,1

    if num:
        return block,0
    return block,1
    

def make_line_list(block):
    point_list = []
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if block[x][y][z]:
                    point_list.append([x,y,z])


    random.shuffle(point_list)

    vis_block = [[[0]*D for i in range(D)] for j in range(D)]

    line_list = []
    while point_list:
        x,y,z = point_list.pop()
        if vis_block[x][y][z]:
            continue

        vis_block[x][y][z] = 1

        sizes = [0]*3
        for i,dir in enumerate(dirs):
            count = 1
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                while in_pos(nx,ny,nz) and block[nx][ny][nz] and vis_block[nx][ny][nz] == 0:
                    count += 1
                    nx,ny,nz = nx+dx,ny+dy,nz+dz
            
            sizes[i] = count
        
        if sum(sizes) == 3:
            lines = [[x,y,z]]
        else:
            cands = []
            for i in range(3):
                if sizes[i] != 1:
                    cands.append(i)
            
            rind = cands[random.randint(0,len(cands)-1)]

            dir = dirs[rind]
            lines = [[x,y,z]]
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                while in_pos(nx,ny,nz) and block[nx][ny][nz] and vis_block[nx][ny][nz] == 0:
                    lines.append([nx,ny,nz])
                    vis_block[nx][ny][nz] = 1
                    nx,ny,nz = nx+dx,ny+dy,nz+dz

            lines.sort()
        line_list.append(lines)
            
    line_split_list = [[] for i in range(D+1)]
    for line in line_list:
        line_split_list[len(line)].append(line)

    return line_split_list


def matching_lines(line_split_lists,num_blocks,new_blocks):

    blocks = copy.deepcopy(new_blocks)
    line_split_0,line_split_1 = line_split_lists
    ### remove same size of line blocks from both 
    for i in range(D+1):
        while line_split_0[i] and line_split_1[i]:
            num_blocks += 1

            block_list = line_split_0[i].pop()
            for x,y,z in block_list:
                blocks[0][x][y][z] = num_blocks
            
            block_list = line_split_1[i].pop()
            for x,y,z in block_list:
                blocks[1][x][y][z] = num_blocks

    for i in range(D+1)[::-1]:

        while line_split_0[i] and line_split_1[i]:
            num_blocks += 1

            block_list = line_split_0[i].pop()
            for x,y,z in block_list:
                blocks[0][x][y][z] = num_blocks
            
            block_list = line_split_1[i].pop()
            for x,y,z in block_list:
                blocks[1][x][y][z] = num_blocks

        if line_split_0[i]:
            
            for line_list in line_split_0[i]:

                pair_cand2 = []
                pair_cand1 = []
                for x in range(1,i+1):
                    y = i-x
                    if x > y:
                        break
                    if x == y:
                        if len(line_split_1[x]) > 1:
                            pair_cand2.append([1/x+1/y,x,y])
                        elif line_split_1[x]:
                            pair_cand1.append([1/x+1/y,x])
                        
                        continue

                    if line_split_1[x] and line_split_1[y]:
                        pair_cand2.append([1/x+1/y,x,y])
                    elif line_split_1[x]:
                        pair_cand1.append([1/x+1/y,x])
                    elif line_split_1[y]:
                        pair_cand1.append([1/x+1/y,y])

                if pair_cand2:
                    pair_cand2.sort()
                    pair = pair_cand2[0]

                    for x in pair[1:]:
                        line_pair = line_split_1[x].pop()

                        num_blocks += 1
                        while line_pair:
                            a,b,c = line_pair.pop()
                            blocks[1][a][b][c] = num_blocks
                            a,b,c = line_list.pop()
                            blocks[0][a][b][c] = num_blocks
                elif pair_cand1:
                    pair_cand1.sort()
                    pair = pair_cand1[0]

                    for x in pair[1:]:
                        line_pair = line_split_1[x].pop()

                        num_blocks += 1
                        while line_pair:
                            a,b,c = line_pair.pop()
                            blocks[1][a][b][c] = num_blocks
                            a,b,c = line_list.pop()
                            blocks[0][a][b][c] = num_blocks
                    line_split_0[len(line_list)].append(line_list)

                # else:
                #     assert False, "line split of 1 is empty"

        elif line_split_1[i]:

            for line_list in line_split_1[i]:
    
                pair_cand2 = []
                pair_cand1 = []
                for x in range(1,i+1):
                    y = i-x
                    if x > y:
                        break

                    if x == y:
                        if len(line_split_0[x]) > 1:
                            pair_cand2.append([1/x+1/y,x,y])
                        elif line_split_0[x]:
                            pair_cand1.append([1/x+1/y,x])
                        
                        continue

                    if line_split_0[x] and line_split_0[y]:
                        pair_cand2.append([1/x+1/y,x,y])
                    elif line_split_0[x]:
                        pair_cand1.append([1/x+1/y,x])
                    elif line_split_0[y]:
                        pair_cand1.append([1/x+1/y,y])

                if pair_cand2:
                    pair_cand2.sort()
                    pair = pair_cand2[0]

                    for x in pair[1:]:
                        line_pair = line_split_0[x].pop()

                        num_blocks += 1
                        while line_pair:
                            a,b,c = line_pair.pop()
                            blocks[0][a][b][c] = num_blocks
                            a,b,c = line_list.pop()
                            blocks[1][a][b][c] = num_blocks
                elif pair_cand1:
                    pair_cand1.sort()
                    pair = pair_cand1[0]

                    for x in pair[1:]:
                        line_pair = line_split_0[x].pop()

                        num_blocks += 1
                        while line_pair:
                            a,b,c = line_pair.pop()
                            blocks[0][a][b][c] = num_blocks
                            a,b,c = line_list.pop()
                            blocks[1][a][b][c] = num_blocks
                    line_split_1[len(line_list)].append(line_list)

                # else:
                #     assert False, "line split of 0 is empty"
    return blocks,num_blocks

best_ans = Output(nmax,base_blocks)
base_num_blocks = num_blocks[:]

fixed_blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]
Xuses = [[[0]*D for i in range(D)] for j in range(2)]
Yuses = [[[0]*D for i in range(D)] for j in range(2)]
num_block = 0


def decide_point(id):
    
    

    random.shuffle(xrange)
    random.shuffle(yrange)
    random.shuffle(zrange)

    for x in xrange:
        for y in yrange:
            for z in zrange:
                if invalid_blocks[id][x][y][z] or fixed_blocks[id][x][y][z]:
                    continue
                if Xuses[id][z][x] and Yuses[id][z][y]:
                    continue

                return x,y,z

    return -1,-1,-1



def calc_block(search_point_list,fixed_block,id):
    
    point_list = []
    block = [[[0]*D for i in range(D)] for j in range(D)]
    for z in range(D):
        xuse = [0]*D
        yuse = [0]*D
        for x in range(D):
            for y in range(D):
                if fixed_block[x][y][z]:
                    xuse[x] = 1
                    yuse[y] = 1
        
        for x in range(D):
            for y in range(D):
                if f[id][z][x] and r[id][z][y] and (xuse[x]*yuse[y] == 0):
                    point_list.append([x,y,z])
                    block[x][y][z] = 1
                    xuse[x] = 1
                    yuse[y] = 1

    random.shuffle(point_list)

    vis_block = [[[0]*D for i in range(D)] for j in range(D)]

    line_list = []

    penalty = 1/len(search_point_list[0])
    while point_list:
        x,y,z = point_list.pop()
        if vis_block[x][y][z]:
            continue

        vis_block[x][y][z] = 1

        sizes = [0]*3
        for i,dir in enumerate(dirs):
            count = 1
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                while in_pos(nx,ny,nz) and block[nx][ny][nz] and vis_block[nx][ny][nz] == 0:
                    count += 1
                    nx,ny,nz = nx+dx,ny+dy,nz+dz
            
            sizes[i] = count
        
        if sum(sizes) == 3:
            lines = [[x,y,z]]
        else:
            cands = []
            for i in range(3):
                if sizes[i] != 1:
                    cands.append(i)
            
            rind = cands[random.randint(0,len(cands)-1)]

            dir = dirs[rind]
            lines = [[x,y,z]]
            for dx,dy,dz in dir:
                nx,ny,nz = x+dx,y+dy,z+dz
                while in_pos(nx,ny,nz) and block[nx][ny][nz] and vis_block[nx][ny][nz] == 0:
                    lines.append([nx,ny,nz])
                    vis_block[nx][ny][nz] = 1
                    nx,ny,nz = nx+dx,ny+dy,nz+dz

            # lines.sort()
        penalty += len(lines)
        # line_list.append(lines)

    return penalty

def make_random_block_shape(id,X,Y,Z):
    nid = id^1

    random_point_list = []
    for x in range(D):
        for y in range(D):
            for z in range(D):
                if invalid_blocks[nid][x][y][z] or fixed_blocks[nid][x][y][z]:
                    continue
                random_point_list.append([x,y,z])

    
    random.shuffle(random_point_list)

    best_score = 0
    best_point_list = [[] for i in range(2)]
    search_point_list = []
    loop = 500
    while random_point_list and loop:
        loop -= 1

        x,y,z = random_point_list.pop()

        dir_shuffle_list = dir_list[:]
        s = random.randint(0,2)

        if s == 0:
            a,b = 1,2
        elif s == 1:
            a,b = 0,2
        else:
            a,b = 0,1
        
        if random.randint(0,1) == 1:
            dir_shuffle_list[a],dir_shuffle_list[b] = dir_shuffle_list[a],dir_shuffle_list[b]

        # random.shuffle(dir_shuffle_list)
        for i in [a,b]:
            random.shuffle(dir_shuffle_list[i])

        fixed_blocks[id][X][Y][Z] = 1
        fixed_blocks[nid][x][y][z] = 1

        vis_point_list = [[] for i in range(2)]
        vis_point_list[id].append([X,Y,Z])
        vis_point_list[nid].append([x,y,z])
        q = [[[X,Y,Z],[x,y,z]]]

        while q:
            point_id,point_nid = q.pop()
            x1,y1,z1 = point_id
            x2,y2,z2 = point_nid
            for i,dirs in enumerate(dir_list):
                for j,(dx,dy,dz) in enumerate(dirs):
                    dx2,dy2,dz2 = dir_shuffle_list[i][j]
                    nx1,ny1,nz1 = x1+dx,y1+dy,z1+dz
                    nx2,ny2,nz2 = x2+dx2,y2+dy2,z2+dz2

                    if in_pos(nx1,ny1,nz1) == 0 or in_pos(nx2,ny2,nz2) == 0:
                        continue

                    if invalid_blocks[id][nx1][ny1][nz1] or invalid_blocks[nid][nx2][ny2][nz2]:
                        continue

                    if fixed_blocks[id][nx1][ny1][nz1] or fixed_blocks[nid][nx2][ny2][nz2]:
                        continue

                    fixed_blocks[id][nx1][ny1][nz1] = 1
                    fixed_blocks[nid][nx2][ny2][nz2] = 1
                    vis_point_list[id].append([nx1,ny1,nz1])
                    vis_point_list[nid].append([nx2,ny2,nz2])
                    q.append([[nx1,ny1,nz1],[nx2,ny2,nz2]])


        for i in range(len(vis_point_list[0])):
            x1,y1,z1 = vis_point_list[0][i]
            x2,y2,z2 = vis_point_list[1][i]
            fixed_blocks[0][x1][y1][z1] = 0
            fixed_blocks[1][x2][y2][z2] = 0    

        le = len(vis_point_list[0])
        if le > 2:
            search_point_list.append(vis_point_list)

            # if le <= 5:
            #     search_point_list.append(vis_point_list)
            # else:
            #     # if random.randint(0,1) == 1:
            #     ind = random.randint(6,le)
            #     search_point_list.append(vis_point_list[:ind])
        # if best_score < len(vis_point_list[0]):
        #     best_score = len(vis_point_list[0])
        #     best_point_list = vis_point_list

    search_point_list.sort(key= lambda x: -len(x[0]))

    best_score = 1000
    # if search_point_list:
    #     return search_point_list[0]
    # else:
    #     return best_point_list
    for i in range(min(len(search_point_list),5)):
        new_score = calc_block(search_point_list[i],fixed_blocks[nid],nid)
        if best_score > new_score:
            best_score = new_score
            best_point_list = search_point_list[i]

    # print(best_score)
    return best_point_list

def make_greedy_ans(new_fixed_blocks,new_Xuses,new_Yuses,new_num_block):

    new_invalid_blocks = copy.deepcopy(invalid_blocks)
    for i in range(2):
        for x in range(D):
            for y in range(D):
                for z in range(D):
                    if new_fixed_blocks[i][x][y][z]:
                        new_invalid_blocks[i][x][y][z] = 1


    
    
    num_blocks = [0,0]
    blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]
    nmax = 0
    for i in range(2):
        n = 0
        for z in range(D):
            for x in range(D):
                for y in range(D):
                    if f[i][z][x] and r[i][z][y] and (new_Xuses[i][z][x]*new_Yuses[i][z][y] == 0):
                        n += 1
                        blocks[i][x][y][z] = n
                        new_Xuses[i][z][x] = 1
                        new_Yuses[i][z][y] = 1

        nmax = max(nmax,n)
        num_blocks[i] = n

    blocks,num_blocks = add_single_point(blocks,num_blocks,new_invalid_blocks)
    dx = abs(num_blocks[0]-num_blocks[1])
    if num_blocks[0] < num_blocks[1]:
        blocks[0],valid = add_block(blocks[0],dx,0,new_invalid_blocks)
    else:
        blocks[1],valid = add_block(blocks[1],dx,1,new_invalid_blocks)

    if valid == 0:
        return -1,-1
    line_split_lists = [make_line_list(blocks[i]) for i in range(2)]
    new_blocks,new_num = matching_lines(line_split_lists,new_num_block,new_fixed_blocks)

    return new_blocks,new_num

def update_blocks(fixed_blocks,Xuses,Yuses,num_block,best_point_list):

    new_fixed_blocks = copy.deepcopy(fixed_blocks)
    new_Xuses = copy.deepcopy(Xuses)
    new_Yuses = copy.deepcopy(Yuses)
    new_num_block = num_block

    new_num_block += 1
    
    
    for i in range(2):
        # assert best_point_list[i]
        # print(best_point_list[i])
        for x,y,z in best_point_list[i]:
            new_fixed_blocks[i][x][y][z] = new_num_block
            new_Xuses[i][z][x] = 1
            new_Yuses[i][z][y] = 1

    new_blocks,new_num = make_greedy_ans(new_fixed_blocks,copy.deepcopy(new_Xuses),copy.deepcopy(new_Yuses),new_num_block)

    return new_blocks,new_num,new_Xuses,new_Yuses,new_num_block,new_fixed_blocks

all_loop = 0
last_all_upd = 0
fixed_blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]
Xuses = [[[0]*D for i in range(D)] for j in range(2)]
Yuses = [[[0]*D for i in range(D)] for j in range(2)]
num_block = 0
while time.time() - stime < TIME_LIM-0.5:


    last_upd = 0
    loop = 0
    temp_ans = Output(nmax,base_blocks)
    while time.time() - stime < TIME_LIM-0.5:
        loop += 1
        # all_loop += 1
        ### decide point of make new blocks TODO 
        id = random.randint(0,1)
        x,y,z = decide_point(id)
        if x == -1:
            if loop - last_upd > 20:
                break
            continue


        best_point_list = make_random_block_shape(id,x,y,z)
        if len(best_point_list[0]) <= 2:
            if loop - last_upd > 20:
                break
            continue


        
        new_blocks,new_num,new_Xuses,new_Yuses,new_num_block,new_fixed_blocks = update_blocks(fixed_blocks,Xuses,Yuses,num_block,best_point_list)

        if new_blocks == -1:
            if loop - last_upd > 20:
                break
            continue
        new_score = calc_score(new_blocks,new_num)
        if new_score < temp_ans.best_score:
            temp_ans.update_best_decide(new_num,new_blocks,new_score)
            fixed_blocks = new_fixed_blocks
            Xuses = new_Xuses
            Yuses = new_Yuses
            num_block = new_num_block

            # temp_ans.out_ans_debug()
            last_upd = loop

            # if new_score < best_ans.best_score:
            #     print("Yes",new_score)
            #     # temp_ans.out_ans_debug()


            

        else:
            if loop - last_upd > 20:
                break

    all_loop += 1
    if best_ans.best_score > temp_ans.best_score:
        last_all_upd = all_loop
        # print(time.time()-stime,temp_ans.best_score)
        # temp_ans.out_ans_debug()
        best_ans = temp_ans


    if all_loop - last_all_upd <= 20:
        num_block = 0
        for x in range(D):
            for y in range(D):
                for z in range(D):
                    num_block = max(num_block,fixed_blocks[0][x][y][z])
        sizes = [0]*num_block
        for x in range(D):
            for y in range(D):
                for z in range(D):
                    id = fixed_blocks[0][x][y][z]
                    if id:
                        sizes[id-1] += 1


        erase = [0]*len(sizes)
        num_block = 0
        Xuses = [[[0]*D for i in range(D)] for j in range(2)]
        Yuses = [[[0]*D for i in range(D)] for j in range(2)]

        cap = max(TIME_LIM - (time.time()-stime),1)
        for i,size in enumerate(sizes):
            if random.random() > 1/size*cap:
                num_block += 1
                erase[i] = num_block
        
        for i in range(2):
            for x in range(D):
                for y in range(D):
                    for z in range(D):
                        id = fixed_blocks[i][x][y][z]
                        if id == 0 or erase[id-1] == 0:
                            fixed_blocks[i][x][y][z] = 0
                            continue

                        fixed_blocks[i][x][y][z] = erase[id-1]
                        Xuses[i][z][x] = 1
                        Yuses[i][z][y] = 1


    else:
        # print(time.time()-stime)
        fixed_blocks = [[[[0]*D for i in range(D)] for j in range(D)] for k in range(2)]
        Xuses = [[[0]*D for i in range(D)] for j in range(2)]
        Yuses = [[[0]*D for i in range(D)] for j in range(2)]
        num_block = 0
# print(f"loop = {all_loop}")
# print(all_loop)
    
# best_ans = Output(num_block,fixed_blocks)
# base_num_blocks = num_blocks[:]

    


best_ans.out_ans()  