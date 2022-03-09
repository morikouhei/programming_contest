import sys
from collections import deque

n = int(input())
M = 30
room = [[1]*M for i in range(M)]
PetType = []
PetPosition = []
HumanPosition = []

movedic = {"U":[-1,0],"D":[1,0],"L":[0,-1],"R":[0,1],".":[0,0]}

movedic2 = {"u":[-1,0],"d":[1,0],"l":[0,-1],"r":[0,1],".":[0,0]}
for i in range(n):
    px,py,pt = map(int,input().split())
    px -= 1
    py -= 1
    PetType.append(pt)
    PetPosition.append([px,py])

m = int(input())
for i in range(m):
    hx,hy = map(int,input().split())
    hx -= 1
    hy -= 1
    HumanPosition.append([hx,hy])



target = [[2,0],[7,29],[13,0],[19,29],[25,0]]
othertarget = [[29,21],[14,8],[14,21],[26,8],[26,21]]
move_range = [[],[[0,9]],[[0,4],[5,9]],[[0,2],[3,6],[7,9]],[[0,1],[2,3],[4,6],[7,9]],[[0,1],[2,3],[4,5],[6,7],[8,9]]]
next_position = [[-1,-1] for i in range(m)]

target2 = [4,10,16,22,28]
move_index = [2,5,8,11,14,17,20,23,26,29]
start_from = [0]*m
direction = [0]*m
turn = 0
workstatus = [0]*(10)
ready_human = []

def canBlock(x,y):
    if x < 0 or x >= M or y < 0 or y >= M:
        return -1
    if room[x][y] == 0:
        return 0

    for px,py in PetPosition:
        if abs(px-x) <= 1 and abs(py-y) <= 1:
            return -1

    for hx,hy in HumanPosition:
        if hx == x and hy == y:
            return -1

    return 1


def canMove(x,y,move_string):
    for s in move_string:
        if s == ".":
            continue
        dx,dy = movedic[s]
        x += dx
        y += dy
        if room[x][y] == 0:
            return False
    return True


def moved_position(x,y,move_string):
    for s in move_string:
        dx,dy = movedic[s]
        x += dx
        y += dy

    return x,y

def PositionUpdate(output):
    for i,s in enumerate(output):
        if s == ".":
            continue
        if s in "udlr":
            dx,dy = movedic2[s]
            hx,hy = HumanPosition[i]
            room[hx+dx][hy+dy] = 0
        else:
            dx,dy = movedic[s]
            hx,hy = HumanPosition[i]
            HumanPosition[i] = [hx+dx,hy+dy]

    print(output)
    sys.stdout.flush()
    PetMove = input().split()
    for i,p in enumerate(PetMove):
        px,py = PetPosition[i]
        px,py = moved_position(px,py,p)
        PetPosition[i] = [px,py]

def bfs(x,y):
    space = [[0]*M for i in range(M)]
    space[x][y] = 1
    q = deque([[x,y]])
    while q:
        nx,ny = q.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = nx+dx
            nny = ny+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and space[nnx][nny] == 0:
                space[nnx][nny] = 1
                q.append([nnx,nny])

    for i in range(n):
        px,py = PetPosition[i]
        if space[px][py]:
            return 0

    return 1

def bfs2(x,y):
    space = [[0]*M for i in range(M)]
    space[x][y] = 1
    q = deque([[x,y]])
    while q:
        nx,ny = q.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = nx+dx
            nny = ny+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and space[nnx][nny] == 0:
                space[nnx][nny] = 1
                q.append([nnx,nny])
    count = 0
    for i in range(n):
        px,py = PetPosition[i]
        if space[px][py]:
            count += 1
    
    num = 0
    for i in range(M):
        num += sum(space[i])

    if num > 30:
        return 0

    return count

def bfs3(sx,sy,gx,gy):
    dis = [[M*5]*M for i in range(M)]
    dis[gx][gy] = 0
    q = deque([[gx,gy]])

    while q:
        x,y = q.popleft()
        
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = x+dx
            nny = y+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and dis[nnx][nny] > dis[x][y]+1:
                dis[nnx][nny] = dis[x][y]+1
                q.append([nnx,nny])

    d = dis[sx][sy]
    for s in "UDLR":
        dx,dy = movedic[s]
        nnx = sx+dx
        nny = sy+dy
        if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and dis[nnx][nny] < d:
            return s

    return "."


def bfs4(ind1,ind2):

    hx1,hy1 = HumanPosition[ind1]
    hx2,hy2 = HumanPosition[ind2]

    dis1 = [[M*5]*M for i in range(M)]
    dis1[hx1][hy1] = 0
    q = deque([[hx1,hy1]])

    while q:
        x,y = q.popleft()
        
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = x+dx
            nny = y+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and dis1[nnx][nny] > dis1[x][y]+1:
                dis1[nnx][nny] = dis1[x][y]+1
                q.append([nnx,nny])

    dis2 = [[M*5]*M for i in range(M)]
    dis2[hx2][hy2] = 0
    q = deque([[hx2,hy2]])

    while q:
        x,y = q.popleft()
        
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = x+dx
            nny = y+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and dis2[nnx][nny] > dis2[x][y]+1:
                dis2[nnx][nny] = dis2[x][y]+1
                q.append([nnx,nny])

    
    mi1 = M*5
    mind = -1
    for i in range(M):
        d = max(dis1[i][8],dis2[i][21])
        if d < mi1:
            mi1 = d
            mind = i

    mi2 = M*5
    mind2 = -1
    for i in range(M):
        d = max(dis2[i][8],dis1[i][21])
        if d < mi2:
            mi2 = d
            mind2 = i

    if mi2 < mi1:
        mind = mind2
        out1 = bfs3(hx1,hy1,mind,21)
        out2 = bfs3(hx2,hy2,mind,8)
        return out1,out2

    else:

        out1 = bfs3(hx1,hy1,mind,8)
        out2 = bfs3(hx2,hy2,mind,21)
        return out1,out2


    
 

def score(x,y):

    space = [[0]*M for i in range(M)]
    space[x][y] = 1
    q = deque([[x,y]])
    while q:
        nx,ny = q.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = nx+dx
            nny = ny+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and space[nnx][nny] == 0:
                space[nnx][nny] = 1
                q.append([nnx,nny])
    count = 0
    for i in range(n):
        px,py = PetPosition[i]
        if space[px][py]:
            count += 1
    
    num = 0
    for i in range(M):
        num += sum(space[i])

    s = 10**8*num//900//pow(2,count)

    return s


def putcheck(out,status,ind):
    global next_position
    hx,hy = HumanPosition[ind]
    assert out in "udlr"

    dx,dy = movedic2[out]
    nx,ny = hx+dx,hy+dy
    for i in range(m):
        x,y = next_position[i]
        if x == nx and y == ny:
            return ".",0


    return out,status


def putcheck2(out,status,ind):
    global next_position
    hx,hy = HumanPosition[ind]
    assert out in "udlr"

    dx,dy = movedic2[out]
    nx,ny = hx+dx,hy+dy
    for i in range(m):
        x,y = next_position[i]
        if x == nx and y == ny:
            return ".",0

    if out not in "lr":
        return out,status

    nx,ny = nx+dx,ny+dy

    space = [[0]*M for i in range(M)]
    space[nx][ny] = 1
    q = deque([[nx,ny]])
    while q:
        nx,ny = q.popleft()
        for dx,dy in zip([1,-1,0,0],[0,0,1,-1]):
            nnx = nx+dx
            nny = ny+dy
            if 0 <= nnx < M and 0 <= nny < M and room[nnx][nny] and space[nnx][nny] == 0:
                space[nnx][nny] = 1
                q.append([nnx,nny])

    for i in range(m):
        hx,hy = HumanPosition[i]
        if space[hx][hy]:
            return ".",0

        hx,hy = next_position[i]
        if hx != -1 and space[hx][hy]:
            return ".",0



    return out,status
### move to start position
def move0(ind):
    if ind < 5:
        x,y = HumanPosition[ind]
        tx,ty = target[ind]
        out = bfs3(x,y,tx,ty)
        if out == ".":
            return out,1
        else:
            return out,0

    else:
        x,y = HumanPosition[ind]
        tx,ty = othertarget[ind-5]
        out = bfs3(x,y,tx,ty)
        if out == ".":
            return out,1
        else:
            return out,0



def first_move():
    hx,hy = HumanPosition[0]
    if hy == M-1:
        return ".",1

    if hy != 8 and hy != 21:
        return "R",0

    if hx == 1 or hx == 2:
        if room[hx-1][hy-1] == 1:
            return "U",0

    if hx == 2 and room[hx-1][hy-1] == 0:
        return "R",0
    
    check1 = canBlock(hx,hy-1)
    check2 = canBlock(hx,hy+1)
    if check1 == 1:
        return putcheck("l",0,0)
       
    elif check2 == 1:
        return putcheck("r",0,0)

    elif check1 == 0 and check2 == 0:
        return "D",0

    return ".",0


def move1(ind):

    if ind == 0:
        return first_move()
    if ind < 5:
        hx,hy = HumanPosition[ind]
        if ind%2:

            if hy == 7 or hy == 9 or hy == 20 or hy == 22:
                return "L",0

            if hy == 8 or hy == 21:
                check = canBlock(hx,hy+1)
                if check == 1:
                    return putcheck("r",0,ind)
                elif check == -1:
                    return ".",0
                else:
                    return "L",0
                

            if hy == 6 or hy == 19:
                check = canBlock(hx,hy+1)
                if check == 1:
                    return putcheck("r",0,ind)
                elif check == -1:
                    return ".",0

            
            check = canBlock(hx-1,hy)
            if check == 1:
                return putcheck("u",0,ind)
            elif check == 0:
                if hy == 0:
                    return ".",1
                else:
                    return "L",0
            else:
                return ".",0

                
        else:
            if hy == 7 or hy == 9 or hy == 20 or hy == 22:
                return "R",0

            if hy == 8 or hy == 21:
                check = canBlock(hx,hy-1)
                if check == 1:
                    return putcheck("l",0,ind)
                elif check == -1:
                    return ".",0
                else:
                    return "R",0
                
            if hy == 10 or hy == 23:
                check = canBlock(hx,hy-1)
                if check == 1:
                    return putcheck("l",0,ind)
                elif check == -1:
                    return ".",0

            check = canBlock(hx-1,hy)
            if check == 1:
                return putcheck("u",0,ind)
            elif check == 0:
                if hy == M-1:
                    return  ".",1
                else:
                    return "R",0
            else:
                return  ".",0

    else:
        return ".",1


def move2(ind):
    hx,hy = HumanPosition[ind]
    if ind < 5:
        if ind%2:
            if hx < target2[ind]:
                return "D",0

            if hy == 7 or hy == 9 or hy == 20 or hy == 22:
                return "R",0

            if hy == 8 or hy == 21:
                check = canBlock(hx,hy-1)
                if check == 1:
                    return putcheck("l",0,ind)
                elif check == -1:
                    return ".",0
                else:
                    return  "R",0
                
            if hy == 10 or hy == 23:
                check = canBlock(hx,hy-1)
                if check == 1:
                    return "l",0
                elif check == -1:
                    return  ".",0

            check = canBlock(hx-1,hy)
            if check == 1:
                return putcheck("u",0,ind)
            elif check == 0:
                if hy == M-1:
                    return  ".",1
                else:
                    return  "R",0

            else:
                return ".",0

        else:
            if hx < target2[ind]:
                return "D",0

            if hy == 7 or hy == 9 or hy == 20 or hy == 22:
                return  "L",0

            if hy == 8 or hy == 21:
                check = canBlock(hx,hy+1)
                if check == 1:
                    return putcheck("r",0,ind)
                elif check == -1:
                    return  ".",0
                else:
                    return  "L",0
                
            if hy == 6 or hy == 19:
                check = canBlock(hx,hy+1)
                if check == 1:
                    return putcheck("r",0,ind)
                elif check == -1:
                    return  ".",0
            
            check = canBlock(hx-1,hy)
            if check == 1:
                return putcheck("u",0,ind)
            elif check == 0:
                if hy == 0:
                    return ".",1
                else:
                    return  "L",0
            else:
                return  ".",0
    else:
        return ".",1


def move3(ind):
    start = start_from[ind]
    start_from[ind] += 1
    if ind < 5:
        if start == 0:
            return "D",0
        elif 0 < start < 9:
            if ind%2:
                return "L",0
            else:
                return "R",0
        else:
            if ind == 4:
                return ".",1
            
            done = int(start == 12)
            if ind%2:
                return "U",done
            else:
                return "D",done

    else:
        return ".",1


ready = 0
blocks = 0


def move4(ind1,ind2,num=-1):
    global blocks
    global ready
    global ready_human
    global turn
    hx,hy = HumanPosition[ind1]
    hx1,hy1 = HumanPosition[ind1]
    hx2,hy2 = HumanPosition[ind2]
    swap = 0
    if hy1 > hy2:
        ind1,ind2 = ind2,ind1
        hx1,hy1,hx2,hy2 = hx2,hy2,hx1,hy1
        swap = 1

    if hx1 != hx2 or hy1 != 8 or hy2 != 21:
        out1,out2 = bfs4(ind1,ind2)
        if swap:
            out1,out2 = out2,out1
        return out1,out2

    
    target_top, target_bottom = move_range[ready][num]
    target_top,target_bottom = move_index[target_top],move_index[target_bottom]

    if hx%3 == 2:
        

        check1 = canBlock(hx1,hy1+1)
        check2 = canBlock(hx2,hy2-1)
        cand1 = 0
        cand2l = 0
        cand2r = 0
        if check1 == 1 and check2 == 1:
            room[hx1][hy1+1] = 0
            room[hx2][hy2-1] = 0
            cand1 = bfs2(hx1,hy1+2)
            room[hx1][hy1+1] = 1
            room[hx2][hy2-1] = 1

        
        check1 = canBlock(hx1,hy1-1)
        check2 = canBlock(hx2,hy2+1)
        

        if check1 == 1:
            room[hx1][hy1-1] = 0
            cand2l += bfs2(hx1,0)
            room[hx1][hy1-1] = 1
        if check2 == 1:
            room[hx2][hy2+1] = 0
            cand2r += bfs2(hx2,29)
            room[hx2][hy2+1] = 1
        cand2 = cand2l+cand2r

        if cand1 > cand2 and blocks < 9:
            if cand1 > 1 or turn >= 150:
                room[hx1][hy1+1] = 0
                room[hx2][hy2-1] = 0
                out1,_ = putcheck2("r",0,ind1)
                out2,_ = putcheck2("l",0,ind2)
                room[hx1][hy1+1] = 1
                room[hx2][hy2-1] = 1
                if out1 != "." and out2 != ".":

                    blocks += 1
                    room[hx1][hy1+1] = 0
                    room[hx2][hy2-1] = 0
                    if swap:
                        return "l","r"
                    return "r","l"

        if cand2:
            out1,out2 = ".","."
            if cand2l:
                room[hx1][hy1-1] = 0
                out1,_ = putcheck2("l",0,ind1)
                room[hx1][hy1-1] = 1
                if out1 != ".":
                    room[hx1][hy1-1] = 0
                    

            if cand2r:
                room[hx2][hy2+1] = 0
                out2,_ = putcheck2("r",0,ind2)
                room[hx2][hy2+1] = 1
                if out2 != ".":
                    room[hx2][hy2+1] = 0

            if out1 != "." or out2 != ".":
                if swap:
                    out1,out2 = out2,out1
                return out1,out2



    if hx < target_top:
        return "D","D"
    if hx > target_bottom:
        return "U","U"

    if hx == target_top:
        direction[ind1] = direction[ind2] = -1
    if hx == target_bottom:
        direction[ind1] = direction[ind2] = 1

    if target_top < hx < target_bottom:
        if direction[ind1] == 0:
            direction[ind1] = direction[ind2] = 1

    move_dir = direction[ind1]

    if hx%3 != 2:
        if move_dir == 1:
            return "U","U"
        else:
            return "D","D"

    else:

        hx1,hy1 = HumanPosition[ind1]
        hx2,hy2 = HumanPosition[ind2]

        check1 = canBlock(hx1,hy1+1)
        check2 = canBlock(hx2,hy2-1)
        cand1 = 0
        cand2l = 0
        cand2r = 0
        if check1 == 1 and check2 == 1:
            room[hx1][hy1+1] = 0
            room[hx2][hy2-1] = 0
            cand1 = bfs2(hx1,hy1+2)
            room[hx1][hy1+1] = 1
            room[hx2][hy2-1] = 1

        
        check1 = canBlock(hx1,hy1-1)
        check2 = canBlock(hx2,hy2+1)
        

        if check1 == 1:
            room[hx1][hy1-1] = 0
            cand2l += bfs2(hx1,0)
            room[hx1][hy1-1] = 1
        if check2 == 1:
            room[hx2][hy2+1] = 0
            cand2r += bfs2(hx2,29)
            room[hx2][hy2+1] = 1
        cand2 = cand2l+cand2r

        if cand1 > cand2 and blocks < 9:
            if cand1 > 1 or turn >= 150:
                room[hx1][hy1+1] = 0
                room[hx2][hy2-1] = 0
                out1,_ = putcheck2("r",0,ind1)
                out2,_ = putcheck2("l",0,ind2)
                room[hx1][hy1+1] = 1
                room[hx2][hy2-1] = 1
                if out1 != "." and out2 != ".":

                    blocks += 1
                    room[hx1][hy1+1] = 0
                    room[hx2][hy2-1] = 0
                    if swap:
                        return "l","r"
                    return "r","l"

        if cand2:
            out1,out2 = ".","."
            if cand2l:
                room[hx1][hy1-1] = 0
                out1,_ = putcheck2("l",0,ind1)
                room[hx1][hy1-1] = 1
                if out1 != ".":
                    room[hx1][hy1-1] = 0
                    

            if cand2r:
                room[hx2][hy2+1] = 0
                out2,_ = putcheck2("r",0,ind2)
                room[hx2][hy2+1] = 1
                if out2 != ".":
                    room[hx2][hy2+1] = 0
            if swap:
                out1,out2 = out2,out1
            return out1,out2
        if cand1 or cand2: 
            if cand2 or cand1 > 1 or turn >= 150:
                return ".","."

  

        if move_dir == 1:
            return "U","U"
        else:
            return "D","D"
           


def move5(ind1):
    hx,hy = HumanPosition[ind1]

    if hy == 21:
        check1 = canBlock(hx,hy+1)
        nx,ny = hx,hy+1
        nny = ny+1
        out = "r"
    else:
        check1 = canBlock(hx,hy-1)
        nx,ny = hx,hy-1
        nny = ny-1
        out = "l"

    cand = 0
    if check1 == 1:
        room[nx][ny] = 0
        cand = bfs2(hx,nny)
        room[nx][ny] = 1
  
    if cand:
        room[nx][ny] = 0
        out,_ = putcheck(out,0,ind1)
        if out != ".":
            return out,0
        else:
            room[nx][ny] = 1
            return ".",0
    return ".",0
        





def move(ind):
    status = workstatus[ind]
    if status == 0:
        return move0(ind)

    if status == 1:
        return move1(ind)
    
    if status == 2:
        return move2(ind)

    if status == 3:
        return move3(ind)

    if status == 4:
        return ".",0




while True:
    output = ["."]*m
    
    sind = [[workstatus[i],i] for i in range(m)]
    sind.sort()
    next_position = [[-1,-1] for i in range(m)]
    for _,i in sind:
        out,done = move(i)
        hx,hy = HumanPosition[i]
        if done:
            workstatus[i] += 1
            out,done = move(i)

        if out in "UDLR":
            dx,dy = movedic[out]
            next_position[i] = [hx+dx,hy+dy]
        if out in "udlr":
            dx,dy = movedic2[out]
            room[hx+dx][hy+dy] = 0
        if workstatus[i] == 4 and i not in ready_human:
            ready_human.append(i)

        output[i] = out

    ready = 0
    for i in range(len(ready_human)//2):
        ind1 = ready_human[i*2]
        ind2 = ready_human[i*2+1]
        hx1,hy1 = HumanPosition[ind1]
        hx2,hy2 = HumanPosition[ind2]
        if hx1 == hx2 and min(hy1,hy2) == 8 and max(hy1,hy2) == 21:
            ready += 1
        else:
            out1,out2 = move4(ind1,ind2)
            
            output[ind1] = out1
            output[ind2] = out2

            if out1 in "UDLR":
                dx,dy = movedic[out1]
                next_position[ind1] = [hx1+dx,hy1+dy]
            if out2 in "UDLR":
                dx,dy = movedic[out2]
                next_position[ind2] = [hx2+dx,hy2+dy]
    num = 0
    for i in range(len(ready_human)//2):
        ind1 = ready_human[i*2]
        ind2 = ready_human[i*2+1]
        hx1,hy1 = HumanPosition[ind1]
        hx2,hy2 = HumanPosition[ind2]
        if hx1 == hx2 and min(hy1,hy2) == 8 and max(hy1,hy2) == 21:
            out1,out2 = move4(ind1,ind2,num)
            output[ind1] = out1
            output[ind2] = out2
            num += 1

    if len(ready_human)%2:
        out,_ = move5(ready_human[-1])
        output[ready_human[-1]] = out


    output = "".join(output)
    PositionUpdate(output)
    turn += 1
    if turn == 300:
        exit()
        
