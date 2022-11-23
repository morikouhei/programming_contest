import sys
import random
import copy
F = list(map(int,input().split()))
n = 10
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

S = "FBLR"
def out(s):
    print(s)
    sys.stdout.flush()

field = [[0]*n for i in range(n)]

def move(field,s):

    nfield = [[0]*n for i in range(n)]


    if s == "L":
        for i in range(n):
            id = 0
            for j in range(n):
                if field[i][j]:
                    nfield[i][id] = field[i][j]
                    id += 1
    if s == "R":
        for i in range(n):
            id = n-1
            for j in range(n)[::-1]:
                if field[i][j]:
                    nfield[i][id] = field[i][j]
                    id -= 1


    if s == "F":
        for i in range(n):
            id = 0
            for j in range(n):
                if field[j][i]:
                    nfield[id][i] = field[j][i]
                    id += 1

    if s == "B":
        for i in range(n):
            id = n-1
            for j in range(n)[::-1]:
                if field[j][i]:
                    nfield[id][i] = field[j][i]
                    id -= 1

    return nfield


def calc_score(field):
    base = [0]*3
    score = [0]*3

    used = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if field[i][j] == 0 or used[i][j]:
                continue
            used[i][j] = 1
            size = 1
            q = [[i,j]]
            while q:
                x,y = q.pop()
                for dx,dy in dxy:
                    nx,ny = x+dx,y+dy
                    if 0 <= nx < n and 0 <= ny < n and field[x][y] == field[nx][ny] and used[nx][ny] == 0:
                        used[nx][ny] = 1
                        q.append([nx,ny])
                        size += 1
            base[field[i][j]-1] += size
            score[field[i][j]-1] += size**2


    bsum = 0
    for i in range(3):
        bsum += base[i]**2
    count = sum(score)/bsum
    return int(count*10**6)


# def calc_score2(field):
#     base = [0]*3
#     score = 0

#     used = [[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if field[i][j] == 0 or used[i][j]:
#                 continue
#             used[i][j] = 1
#             size = 1
#             q = [[i,j]]
#             while q:
#                 x,y = q.pop()
#                 for dx,dy in dxy:
#                     nx,ny = x+dx,y+dy
#                     if 0 <= nx < n and 0 <= ny < n and field[x][y] == field[nx][ny] and used[nx][ny] == 0:
#                         used[nx][ny] = 1
#                         q.append([nx,ny])
#                         size += 1
#             score += 1


#     return score


def sim_move(field,cand,turn):
    nfield = [f[:] for f in field]

    for t,i in enumerate(cand,turn):
        nfield = update2(nfield,t,i)
        s = S[random.randint(0,3)]
        nfield = move(nfield,s)

    return calc_score(nfield)



def simulate(field,turn):

    depth = min(4,99-turn)

    cands = []
    for i in range(80):
        l = []
        for j in range(depth):
            l.append(random.randint(1,100-turn-j))
        cands.append(l)


    out_s = "L"
    temp_score = 0
    for s in S:
        nfield = move(field,s)

        count = 0

        for cand in cands:
            count += sim_move(nfield,cand,turn)

        if count > temp_score:
            temp_score = count
            out_s = s

    return out_s
    

def update(field,turn):
    p = int(input())
    s = 0
    for i in range(n):
        for j in range(n):
            if field[i][j]:
                continue
            s += 1
            if p == s:
                field[i][j] = F[turn]
                return field

def update2(field,turn,p):
    s = 0
    for i in range(n):
        for j in range(n):
            if field[i][j]:
                continue
            s += 1
            if p == s:
                field[i][j] = F[turn]
                return field

    assert False
for i in range(100):
    field = update(field,i)

    out_s = simulate(field,i+1)
    field = move(field,out_s)


    out(out_s)
# print(calc_score(field))