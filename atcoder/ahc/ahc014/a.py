import time
import random
from heapq import heappop,heappush

stime = time.time()
n,m = map(int,input().split())

area_save = [[0]*n for i in range(n)]

for i in range(m):
    x,y = map(int,input().split())
    area_save[x][y] = 1


Dx1 = [1,0,-1,0,1]
Dy1 = [0,1,0,-1,0]

Dx2 = [1,-1,-1,1,1]
Dy2 = [1,1,-1,-1,1]

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


def pos2ind(x,y):
    return x*n+y

def ind2pos(ind):
    return divmod(ind,x)

def output_answer(output):
    print(len(output))
    for i in output:
        print(*i)

def solve():

    area = [[area_save[i][j] for j in range(n)] for i in range(n)]
    # print(area == area_save)
    uf1 = Unionfind(n**2)
    uf2 = Unionfind(n**2)

    weight_x = [[0]*n for i in range(n)]
    weight_y = [[0]*n for i in range(n)]

    weight_xy = [[0]*n for i in range(n)]
    weight_yx = [[0]*n for i in range(n)]

    output = []


    def calc_score(area):
        cx,cy = n//2,n//2
        count = 0
        all_sum = 0
        for i in range(n):
            for j in range(n):
                w = (i-cx)**2+(j-cy)**2+1
                all_sum += w
                if area[i][j]:
                    count += w
        
        score = 10**6 * (n**2) * count / m / all_sum
        return int(score)

    def nearest_point(x,y,dx,dy):

        nx,ny = x+dx,y+dy
        while 0 <= nx < n and 0 <= ny < n and area[nx][ny] == 0:
            nx,ny = nx+dx,ny+dy

        if 0 <= nx < n and 0 <= ny < n:
            return nx,ny
        else:
            return -1,-1


    def check_loop(Xlis,Ylis,ind,uf_id):

        x1,y1 = Xlis[0],Ylis[0]
        area[x1][y1] = 1

        for i in range(4):
            x,y = Xlis[(ind+i)%4],Ylis[(ind+i)%4]
            nx,ny = Xlis[(ind+i+1)%4],Ylis[(ind+i+1)%4]

            while True:
                if uf_id == 1:
                    x += Dx1[i]
                    y += Dy1[i]
                else:
                    x += Dx2[i]
                    y += Dy2[i]

                if area[x][y]:
                    if (x,y) != (nx,ny):
                        area[x1][y1] = 0
                        return False
                    else:
                        break
        
        area[x1][y1] = 0
        return True

    def calc_weight(x,y,nx,ny,ind):

        count = 0

        if ind == 0:
            while x != nx:
                x += 1
                count += weight_x[x][y]

        if ind == 1:
            while y != ny:
                y += 1
                count += weight_y[x][y]

        if ind == 2:
            while x != nx and y != ny:
                x += 1
                y += 1
                count += weight_xy[x][y]


        if ind == 3:
            while x != nx and y != ny:
                x -= 1
                y += 1
                count += weight_yx[x][y]

        
        return count

    def add_weight(x,y,nx,ny,ind):

        if ind == 0:
            while x != nx:
                x += 1
                weight_x[x][y] += 1

        if ind == 1:
            while y != ny:
                y += 1
                weight_y[x][y] += 1

        if ind == 2:
            while x != nx and y != ny:
                x += 1
                y += 1
                weight_xy[x][y] += 1


        if ind == 3:
            while x != nx and y != ny:
                x -= 1
                y += 1
                weight_yx[x][y] += 1


    def can_line(point_list,uf_id):
        x1,y1 = point_list[:2]
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= n:
            return False
        if area[x1][y1]:
            return False


        Xlis,Ylis = point_list[0::2],point_list[1::2]
        lx = min(Xlis)
        ly = min(Ylis)

        ind = -1
        for i in range(4):
            if Xlis[i] == lx and Ylis[i] == ly:
                ind = i
            elif ind == -1 and Ylis[i] == ly:
                ind = i

        if check_loop(Xlis,Ylis,ind,uf_id) == False:
            return False
       

        if uf_id == 1:
            c1 = calc_weight(lx,ly,Xlis[ind-1],Ylis[ind-1],1)
            c2 = calc_weight(Xlis[ind-3],Ylis[ind-3],Xlis[ind-2],Ylis[ind-2],1)

            c3 = calc_weight(lx,ly,Xlis[ind-3],Ylis[ind-3],0)
            c4 = calc_weight(Xlis[ind-1],Ylis[ind-1],Xlis[ind-2],Ylis[ind-2],0)

        else:
            c1 = calc_weight(Xlis[ind],Ylis[ind],Xlis[ind-1],Ylis[ind-1],3)
            c2 = calc_weight(Xlis[ind-3],Ylis[ind-3],Xlis[ind-2],Ylis[ind-2],3)

            c3 = calc_weight(Xlis[ind],Ylis[ind],Xlis[ind-3],Ylis[ind-3],2)
            c4 = calc_weight(Xlis[ind-1],Ylis[ind-1],Xlis[ind-2],Ylis[ind-2],2)

        if c1+c2+c3+c4:
            return False

        if uf_id == 1:
            ps = [uf1.find(pos2ind(point_list[2*i],point_list[2*i+1])) for i in range(4)]
        else:
            ps = [uf2.find(pos2ind(point_list[2*i],point_list[2*i+1])) for i in range(4)]

        if len(set(ps)) == 4:
            return True
        else:
            return False


    def connect_line(point_list,uf_id):


        if uf_id == 1:
            ps = [uf1.find(pos2ind(point_list[2*i],point_list[2*i+1])) for i in range(4)]
        else:
            ps = [uf2.find(pos2ind(point_list[2*i],point_list[2*i+1])) for i in range(4)]

        x1,y1 = point_list[:2]
        area[x1][y1] = 1


        Xlis,Ylis = point_list[0::2],point_list[1::2]
        lx = min(Xlis)
        ly = min(Ylis)

        ind = -1
        for i in range(4):
            if Xlis[i] == lx and Ylis[i] == ly:
                ind = i
            elif ind == -1 and Ylis[i] == ly:
                ind = i

        if uf_id == 1:
            add_weight(Xlis[ind],Ylis[ind],Xlis[ind-1],Ylis[ind-1],1)
            add_weight(Xlis[ind-3],Ylis[ind-3],Xlis[ind-2],Ylis[ind-2],1)

            add_weight(Xlis[ind],Ylis[ind],Xlis[ind-3],Ylis[ind-3],0)
            add_weight(Xlis[ind-1],Ylis[ind-1],Xlis[ind-2],Ylis[ind-2],0)

        else:
            add_weight(Xlis[ind],Ylis[ind],Xlis[ind-1],Ylis[ind-1],3)
            add_weight(Xlis[ind-3],Ylis[ind-3],Xlis[ind-2],Ylis[ind-2],3)

            add_weight(Xlis[ind],Ylis[ind],Xlis[ind-3],Ylis[ind-3],2)
            add_weight(Xlis[ind-1],Ylis[ind-1],Xlis[ind-2],Ylis[ind-2],2)

        for i in range(3):
            x,y,nx,ny = point_list[2*i:2*i+4]
            if uf_id == 1:
                uf1.union(pos2ind(x,y),pos2ind(nx,ny))
            else:
                uf2.union(pos2ind(x,y),pos2ind(nx,ny))

        output.append(point_list)


    def calc_path_weight(point_list,uf_id):
        weight = 0
        X = point_list[0::2]
        Y = point_list[1::2]

        for i in range(4):
            x,y = X[i],Y[i]
            nx,ny = X[i-1],Y[i-1]
            weight += abs(x-nx)+abs(y-ny)

        return weight // uf_id



    h = []
    

    def h_push(x3,y3):

        for ind in range(4):
            x4,y4 = nearest_point(x3,y3,Dx1[ind],Dy1[ind])
            x2,y2 = nearest_point(x3,y3,Dx1[ind+1],Dy1[ind+1])

            if x4 == -1 or x2 == -1:
                continue

            x1,y1 = x4+x2-x3,y4+y2-y3

            point_list = [x1,y1,x2,y2,x3,y3,x4,y4]
            if can_line(point_list,1):
                weight = calc_path_weight(point_list,1)
                heappush(h,[weight,random.randint(0,10**10),point_list,1])
            
        for ind in range(4):
            x4,y4 = nearest_point(x3,y3,Dx2[ind],Dy2[ind])
            x2,y2 = nearest_point(x3,y3,Dx2[ind+1],Dy2[ind+1])

            if x4 == -1 or x2 == -1:
                continue

            x1,y1 = x4+x2-x3,y4+y2-y3

            point_list = [x1,y1,x2,y2,x3,y3,x4,y4]
            if can_line(point_list,2):
                weight = calc_path_weight(point_list,2)
                heappush(h,[weight,random.randint(0,10**10),point_list,2])


    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                continue
            x3,y3 = i,j
            h_push(x3,y3)


    while h:
        _,_,point_list,uf_id = heappop(h)

        if can_line(point_list,uf_id):
            connect_line(point_list,uf_id)

            x3,y3 = point_list[:2]

            h_push(x3,y3)

            for ind in range(4):
                x4,y4 = nearest_point(x3,y3,Dx1[ind],Dy1[ind])

                if x4 != -1:
                    h_push(x4,y4)

                x4,y4 = nearest_point(x3,y3,Dx2[ind],Dy2[ind])

                if x4 != -1:
                    h_push(x4,y4)
    
    score = calc_score(area)
    return output,score



output,score = solve()

num = 0
# print(score)
while time.time() - stime <= 4.5:
    new_output,new_score = solve()
    if new_score > score:
        output = new_output
        score = new_score
        # print(score,"yes")
    num += 1
output_answer(output)

# print(num)
                

