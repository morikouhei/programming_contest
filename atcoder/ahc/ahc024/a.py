import time

STIME = time.time()
TIME_LIM = 2

n,m = map(int,input().split())

C = [list(map(int,input().split())) for i in range(n)]
C_base = [c[:] for c in C]
dxy = [[1,0],[0,1],[-1,0],[0,-1]]

tiles = [0]*m
for x in range(n):
    for y in range(n):
        c = C[x][y]
        tiles[c-1] += 1


def clean(C):
    h = len(C)
    w = len(C[0])
    for i in range(5):

        for x in range(h):
            for y in range(w):

                c = C[x][y]
                c_base = c
                around = []
                for dx,dy in dxy:
                    nx,ny = x+dx,y+dy

                    if 0 <= nx < h and 0 <= ny < w:
                        around.append(C[nx][ny])
                    else:
                        around.append(0)
                
                sames = around.count(c)
                if sames == 0 or sames > 1:
                    continue

                size = len(set(around))
                if size == 2 or (size == 3 and 0 in around and around.count(c) > 1) :
                    for nc in around:
                        if nc and nc != c:
                            other = nc
                    C[x][y] = other

                    continue

                
                around_set = set()
                for xx in range(x-1,x+2):
                    for yy in range(y-1,y+2):
                        if 0 <= xx < h and 0 <= yy < w:
                            c = C[xx][yy]
                            for dx,dy in dxy:
                                nx,ny = xx+dx,yy+dy
                                if 0 <= nx < h and 0 <= ny < w:
                                    nc = C[nx][ny]
                                else:
                                    nc = 0

                                mi,ma = min(c,nc),max(c,nc)

                                around_set.add((mi,ma))

                for a in set(around):
                    if a == 0 or around.count(a) == 1:
                        continue

                    around_set2 = set()
                    C[x][y] = a

                    for xx in range(x-1,x+2):
                        for yy in range(y-1,y+2):
                            if 0 <= xx < h and 0 <= yy < w:
                                c = C[xx][yy]
                                for dx,dy in dxy:
                                    nx,ny = xx+dx,yy+dy
                                    if 0 <= nx < h and 0 <= ny < w:
                                        nc = C[nx][ny]
                                    else:
                                        nc = 0

                                    mi,ma = min(c,nc),max(c,nc)

                                    around_set2.add((mi,ma))
          

                    if sorted(around_set) != sorted(around_set2):
                        C[x][y] = c_base
                        break



# for c in C_base:
#     print(*c)
# print()


def check_connect(C):

    h = len(C)
    w = len(C[0])
    vis = [[0]*w for i in range(h)]

    sizes = [0]*(m+1)

    for i in range(h):
        for j in range(w):
            if vis[i][j]:
                continue
            c = C[i][j]
            if sizes[c]:
                return 0

            vis[i][j] = 1
            q = [[i,j]]

            while q:
                x,y = q.pop()
                sizes[c] += 1 
                for dx,dy in dxy:
                    nx,ny = x+dx,y+dy
                    
                    if 0 <= nx < h and 0 <= ny < w and C[nx][ny] == c:
                        if vis[nx][ny] == 0:
                            vis[nx][ny] = 1
                            q.append([nx,ny])
    return 1

def comp_C(C):

    h = len(C)
    w = len(C[0])
    C_comp = [C[0]]
    last = 0
    around = [set() for i in range(m)]
    i = 0
    for j in range(w):
        c = C[i][j]
        for dx,dy in dxy:
            nx,ny = i+dx,j+dy
            if dx == 1:
                continue
            if 0 <= nx < h and 0 <= ny < w:
                if C[nx][ny] != c:
                    around[c-1].add(C[nx][ny])
                    around[C[nx][ny]-1].add(c)
            else:
                around[c-1].add(0)

    for i in range(1,h-1):

        around_base = [set() for i in range(m)]
        around_test = [set() for i in range(m)]

        for j in range(w):
            c = C[i][j]
            for dx,dy in dxy:
                nx,ny = i+dx,j+dy

                if dx == -1:
                    nx = last

                if 0 <= nx < h and 0 <= ny < w:
                    if C[nx][ny] != c:
                        around_base[c-1].add(C[nx][ny])
                        around_base[C[nx][ny]-1].add(c)
                else:
                    around_base[c-1].add(0)
                

        for j in range(w):
            c = C[i+1][j]
            for dx,dy in dxy:
                nx,ny = i+1+dx,j+dy

                if dx == -1:
                    nx = last

                else:
                    continue

                
                if dx == -1:
                    if 0 <= nx < h and 0 <= ny < w:
                        if C[nx][ny] != c:
                            # around_base[c-1].add(C[nx][ny])
                            around_test[c-1].add(C[nx][ny])
                            around_test[C[nx][ny]-1].add(c)
                    else:
                        # around_base[c-1].add(0)
                        around_test[c-1].add(0)

                else:
                    if 0 <= nx < h and 0 <= ny < w:
                        if C[nx][ny] != c:
                            around_base[c-1].add(C[nx][ny])
                            around_base[C[nx][ny]-1].add(c)
                            around_test[c-1].add(C[nx][ny])
                            around_test[C[nx][ny]-1].add(c)
                    else:
                        around_base[c-1].add(0)
                        around_test[c-1].add(0)

                

        ok = 1
        # print(i)
        for j in range(m):
            sbase = sorted(around_base[j] | around[j])
            stest = sorted(around_test[j] | around[j])
            if sbase != stest:
                ok = 0
                # print(j,sbase,stest)
        
        
        for j in range(w):
            c = C[i+1][j]
            sames = 0
            for dx,dy in dxy:
                nx,ny = i+1+dx,j+dy

                if dx == -1:
                    nx = last

                if 0 <= nx < h and 0 <= ny < w:
                    if C[nx][ny] == c:
                        sames += 1
                        
            if sames == 0 and tiles[c-1] != 1:
                ok = 0

        if ok:

            test_C = [c[:] for c in C_comp]

            for l in range(i+1,h):
                test_C.append(C[l][:])

            if check_connect(test_C):
                continue
            

        C_comp.append(C[i][:])
        for j in range(w):
            c = C[i][j]
            for dx,dy in dxy:
                nx,ny = i+dx,j+dy
                if dx == 1:
                    continue
                if dx == -1:
                    nx = last

                if 0 <= nx < h and 0 <= ny < w:
                    if C[nx][ny] != c:
                        around[c-1].add(C[nx][ny])
                else:
                    around[c-1].add(0)


        last = i
    C_comp.append(C[-1])

    return C_comp
                



def calc_score(C):
    num = 0
    for c in C:
        num += c.count(0)
    
    return num + 1

def fill_C(C):
    ans = [[0]*n for i in range(n)]
    h = len(C)
    w = len(C[0])

    for i in range(h):
        for j in range(w):
            ans[i][j] = C[i][j]

    return ans
while True:
    clean(C)
    h,w = len(C),len(C[0])
    C = comp_C([c[:] for c in C])

    C = list(zip(*C))
    for i in range(len(C)):
        C[i] = list(C[i])
    nw,nh = len(C),len(C[0])
    if h == nh and w == nw:
        break

    C_comp = fill_C(C)
    for c in C_comp:
        print(*c)
# print(calc_score(C_comp))

C_comp = fill_C(C)
for c in C_comp:
    print(*c)