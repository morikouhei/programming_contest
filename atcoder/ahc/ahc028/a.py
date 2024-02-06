import time
import random

random.seed(998244353)

stime = time.time()
TIME_LIM = 2

INF = 10000
size = 5
n,m = map(int,input().split())
si,sj = map(int,input().split())
A = [list(input()) for i in range(n)]
T = [input() for i in range(m)]

def get_ind(a):
    return ord(a) - ord("A")

def get_cost(x,y,nx,ny):
    return abs(x-nx) + abs(y-ny) + 1

def get_comp_dist(T1,T2):

    assert T1 != T2

    for i in range(1,size):

        ok = 1

        for j in range(i,size):
            if T1[j] != T2[j-i]:
                ok = 0
        if ok:
            return size-i

    return 0

Char_pos_list = [[] for i in range(26)]
for i in range(n):
    for j in range(n):
        ind = get_ind(A[i][j])
        Char_pos_list[ind].append([i,j])

min_dist_list = [[[INF]*26 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):

        for ni in range(n):
            for nj in range(n):
                ind = get_ind(A[ni][nj])

                min_dist_list[i][j][ind] = min(min_dist_list[i][j][ind],get_cost(i,j,ni,nj))


compress_string = [[0]*m for i in range(m)]

for i in range(m):
    for j in range(m):
        if i == j:
            continue

        compress_string[i][j] = get_comp_dist(T[i],T[j])


def get_move(x,y,ns,nns):

    if A[x][y] == ns:
        return [x,y]

    nind = get_ind(ns)
    if nns == "":
        dist_min = INF
        nex = []

        for nx,ny in Char_pos_list[nind]:

            dist = get_cost(x,y,nx,ny)
            if dist_min > dist:
                dist_min = dist
                nex = [nx,ny]

        assert dist_min != INF

    else:
        nnind = get_ind(nns)

        dist_min = INF
        nex = []

        for nx,ny in Char_pos_list[nind]:

            dist = get_cost(x,y,nx,ny) + min_dist_list[nx][ny][nnind]
            if dist_min > dist:
                dist_min = dist
                nex = [nx,ny]

        assert dist_min != INF


    return nex



def get_move2(x,y,ns,nnx,nny):

    if A[x][y] == ns:
        return [x,y]

    nind = get_ind(ns)

    dist_min = INF
    nex = []

    for nx,ny in Char_pos_list[nind]:

        dist = get_cost(x,y,nx,ny) + get_cost(nx,ny,nnx,nny)
        if dist_min > dist:
            dist_min = dist
            nex = [nx,ny]

    assert dist_min != INF


    return nex

used = [0]*m


ans = []
ans_string = []
score = 0
x,y = si,sj

last = -1


link_pre = [-1]*m
link_aft = [-1]*m
move_pos_list = [[] for i in range(m)]

for turn in range(m):

    dist_min = INF
    nind = -1

    for i in range(m):
        if used[i]:
            continue

        if A[x][y] == T[i][0]:
            dist = 0
        else:
            dist = min_dist_list[x][y][get_ind(T[i][0])]

        if dist_min > dist:
            dist_min = dist
            nind = i

    start = 0
    if last != -1:
        start = compress_string[last][nind]

        for i in range(start,0,-1):
            move_pos_list[nind].append(ans[-i])

    for i in range(start,size):
        ns = T[nind][i]
        nns = ""
        if i != size-1:
            nns = T[nind][i+1]

        nex = get_move(x,y,ns,nns)

        ans.append(nex)
        score += get_cost(x,y,nex[0],nex[1])
        x,y = nex
        move_pos_list[nind].append(nex)
    

    link_pre[nind] = last
    if last != -1:
        link_aft[last] = nind

    last = nind
    used[last] = 1

assert sum(used) == m

for i in range(m):
    if link_pre[i] == -1:
        start = i


## 1点移動
def neighbor1():
    global score

    bind = random.randint(0,m-1)

    nind = random.randint(0,m-1)

    if bind == nind or link_pre[bind] == -1 or link_aft[nind] == bind:
        return False

    start_link_pre = link_pre[:]
    start_link_aft = link_aft[:]
    ## bind を nind の後に追加

    base_score = score

    pre_ind = link_pre[bind]
    aft_ind = link_aft[bind]

    if pre_ind != -1:
        if T[pre_ind][-1] == T[bind][0]:
            assert move_pos_list[pre_ind][-1] == move_pos_list[bind][0]

        else:
            x,y = move_pos_list[pre_ind][-1]
            nx,ny = move_pos_list[bind][0]
            base_score -= get_cost(x,y,nx,ny)

    if aft_ind != -1:
        if T[bind][-1] == T[aft_ind][0]:
            assert move_pos_list[bind][-1] == move_pos_list[aft_ind][0]

        else:
            x,y = move_pos_list[bind][-1]
            nx,ny = move_pos_list[aft_ind][0]
            base_score -= get_cost(x,y,nx,ny)

    for i in range(size-1):
        x,y = move_pos_list[bind][i]
        nx,ny = move_pos_list[bind][i+1]
        base_score -= get_cost(x,y,nx,ny)


    aft_ind2 = link_aft[nind]

    if aft_ind2 != -1:
        if T[nind][-1] == T[aft_ind2][0]:
            assert move_pos_list[nind][-1] == move_pos_list[aft_ind2][0]

        else:
            x,y = move_pos_list[nind][-1]
            nx,ny = move_pos_list[aft_ind2][0]
            base_score -= get_cost(x,y,nx,ny)

    
    if pre_ind != -1 and aft_ind != -1:
        if T[pre_ind][-1] == T[aft_ind][0]:
            x,y = move_pos_list[pre_ind][-1]
            nx,ny = move_pos_list[aft_ind][1]
            base_score += get_cost(x,y,nx,ny)
        else:
            x,y = move_pos_list[pre_ind][-1]
            nx,ny = move_pos_list[aft_ind][0]
            base_score += get_cost(x,y,nx,ny)

    nex_pos_list = []
    x,y = move_pos_list[nind][-1]

    for i in range(size):

        if i < size-1 or aft_ind2 == -1:
            ns = T[bind][i]
            nns = T[bind][i+1] if i < size -1 else ""

            nex = get_move(x,y,ns,nns)
        else:
            ns = T[bind][i]
            nnx,nny = move_pos_list[aft_ind2][0]
            nex = get_move2(x,y,ns,nnx,nny)

        nx,ny = nex
        if x == nx and y == ny and i == size-1:
            base_score += 0
        else:
            base_score += get_cost(x,y,nx,ny)
        nex_pos_list.append(nex)
        x,y = nex

    if aft_ind2 != -1 and [x,y] != move_pos_list[aft_ind2][0]:
        base_score += get_cost(x,y,move_pos_list[aft_ind2][1][0],move_pos_list[aft_ind2][1][1])


    if base_score <= score:
        move_pos_list[bind] = nex_pos_list
        
        if T[pre_ind][-1] == T[link_aft[bind]][0]:
            move_pos_list[link_aft[bind]][0] = move_pos_list[pre_ind][-1]
    

        link_aft[pre_ind] = link_aft[bind]
        if link_aft[bind] != -1:
            link_pre[link_aft[bind]] = pre_ind


        link_aft[nind] = bind
        
        if aft_ind != -1:
            link_pre[aft_ind] = bind

        link_aft[bind] = aft_ind
        link_pre[bind] = nind

        if aft_ind != -1 and T[bind][-1] == T[aft_ind][0]:
            move_pos_list[aft_ind][0] = move_pos_list[bind][-1]

        print(bind,nind,base_score,score)
        score = base_score
        return True



    count = [0]*m
    now = start
    for i in range(m):
        count[now] = 1
        now = link_aft[now]
    
    print(bind,nind,score,base_score)
    assert now == -1

    assert sum(count) == m
    assert link_aft == start_link_aft
    assert link_pre == start_link_pre
    assert now == -1 and sum(count) == m

    return False

### 2点SWAP
def neighbor2():

    pass


def out_ans():
    for i in range(m):
        if link_pre[i] == -1:
            now = i

    ans_out = []
    last = ""

    for i in range(m):

        for j in range(size):
            if j == 0 and last == T[now][j]:
                continue

            last = T[now][j]
            ans_out.append(move_pos_list[now][j])
        
        now = link_aft[now]

    for x,y in ans_out:
        print(x,y)

while time.time() - stime < TIME_LIM - 0.1:

    rand = random.randint(0,1)

    if True:

        c = neighbor1()
        if c:
            break


    else:
        neighbor2()

    # out_ans()


out_ans()
        