import time
import random
from collections import deque

stime = time.time()
n,T = map(int,input().split())

## path 0:left [0,-1] 1:up [-1,0] 2:right [0,1], 3:down [1,0]
path = [[0,0,0,0],[1,0,0,0],[0,1,0,0],[1,1,0,0],[0,0,1,0],[1,0,1,0],[0,1,1,0],[1,1,1,0],[0,0,0,1],[1,0,0,1],[0,1,0,1],[1,1,0,1],[0,0,1,1],[1,0,1,1],[0,1,1,1],[1,1,1,1]]
revdic = "0123456789abcdef"
tiles = [[revdic.index(i) for i in input()] for j in range(n)]
moveC = "LURD"
movedic = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1]}
rev_move_dic = {"U":"D","D":"U","L":"R","R":"L"}

Dx = [0,-1,0,1]
Dy = [-1,0,1,0]

def path_check(x,y,nx,ny):

    dx = nx-x
    dy = ny-y

    id1 = tiles[x][y]
    id2 = tiles[nx][ny]
    if dx == 0 and dy == 1:

        if path[id1][2] and path[id2][0]:
            return True
        else:
            return False

    if dx == 0 and dy == -1:
    
        if path[id1][0] and path[id2][2]:
            return True
        else:
            return False

    if dx == 1 and dy == 0:
    
        if path[id1][3] and path[id2][1]:
            return True
        else:
            return False

    if dx == -1 and dy == 0:
        
        if path[id1][1] and path[id2][3]:
            return True
        else:
            return False


def canMove(x,y,move_s):

    dx,dy = movedic[move_s]
    nx = dx + x
    ny = dy + y

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        return -1,-1
    
    return nx,ny


def swap(x,y,move_s):

    nx,ny = canMove(x,y,move_s)
    if nx == -1:
        return False

    tiles[x][y],tiles[nx][ny] = tiles[nx][ny],tiles[x][y]

    return True

def reverse_tile(x,y,move_string):

    for move_s in move_string[::-1]:
        move_s = rev_move_dic[move_s]
        nx,ny = canMove(x,y,move_s)
        swap(x,y,move_s)
        x,y = nx,ny


def calc_score(turn):

    use = [[0]*n for i in range(n)]
    vis = [[[0]*4 for i in range(n)] for j in range(n)]
    bef = [[[-1]*2 for i in range(n)] for j in range(n)]
    max_tree_size = 0

    for i in range(n):
        for j in range(n):
            if use[i][j]:
                continue
            
            if tiles[i][j] == 0:
                continue
            now_size = 1
            find_loop = 0
            q = deque()
            q.append([i,j])
            use[i][j] = 1
            vis[i][j] = [1]*4
            while q:
                x,y = q.popleft()
                for id in range(4):
                    nx,ny = x+Dx[id],y+Dy[id]
                    if bef[x][y] == [nx,ny]:
                        continue
                    if 0 <= nx < n and 0 <= ny < n and path_check(x,y,nx,ny):

                        if vis[nx][ny][(id+2)%4]:
                            continue
                        vis[nx][ny][(id+2)%4] = 1
                        vis[x][y][id] = 1

                        if use[nx][ny]:
                            find_loop = 1
                            continue
                        use[nx][ny] = 1
                        now_size += 1
                        bef[nx][ny] = [x,y]
                        q.append([nx,ny])
            if find_loop:
                now_size = 0
          
            max_tree_size = max(max_tree_size,now_size)
    return max_tree_size

def calc_score2(turn):
    
    use = [[0]*n for i in range(n)]
    vis = [[[0]*4 for i in range(n)] for j in range(n)]
    bef = [[[-1]*2 for i in range(n)] for j in range(n)]
    max_tree_size = 0
    groups = 0
    for i in range(n):
        for j in range(n):
            if use[i][j]:
                continue
            groups += 1
            if tiles[i][j] == 0:
                continue
            now_size = 1
            find_loop = 0
            q = deque()
            q.append([i,j])
            use[i][j] = 1
            vis[i][j] = [1]*4
            while q:
                x,y = q.popleft()
                for id in range(4):
                    nx,ny = x+Dx[id],y+Dy[id]
                    if bef[x][y] == [nx,ny]:
                        continue
                    if 0 <= nx < n and 0 <= ny < n and path_check(x,y,nx,ny):

                        if vis[nx][ny][(id+2)%4]:
                            continue
                        vis[nx][ny][(id+2)%4] = 1
                        vis[x][y][id] = 1

                        if use[nx][ny]:
                            find_loop = 1
                            continue
                        use[nx][ny] = 1
                        now_size += 1
                        bef[nx][ny] = [x,y]
                        q.append([nx,ny])
            if find_loop:
                now_size = 0
          
            max_tree_size = max(max_tree_size,now_size)
    return max_tree_size #+ 10/groups


ans_string = []
max_score = calc_score2(0)

turn = 0
save_tiles = [t[:] for t in tiles]
nums = 0
while time.time() - stime < 2.8:

    for i in range(n):
        for j in range(n):
            if tiles[i][j] == 0:
                x,y = i,j
    
    new_string = []

    new_turn = 0
    now_max = 0
    max_turn = 0
    while new_turn < 10 and turn + new_turn < T:

        move_s = moveC[random.randint(0,3)]
        if swap(x,y,move_s):
            new_turn += 1
            x,y = canMove(x,y,move_s)

            now_score = calc_score2(turn)
            new_string.append(move_s)
            if now_score >= now_max:
                now_max = now_score
                max_turn = new_turn
            
    if now_max > max_score:
        reverse_tile(x,y,new_string[max_turn:])
        max_score = now_max
        for j in range(max_turn):
            ans_string.append(new_string[j])
        turn += max_turn
    else:
        # left = 3+stime-time.time()
        # dif = (left)/3
        # # print(dif)
        # if random.random() < dif:
        #     print(dif)
        #     reverse_tile(x,y,new_string[max_turn:])
        #     max_score = now_max
        #     for j in range(max_turn):
        #         ans_string.append(new_string[j])
        #     turn += max_turn
        # else:
        reverse_tile(x,y,new_string)

print("".join(ans_string))



