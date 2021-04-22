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


h,w = map(int,input().split())
uf = Unionfind(h*w)
color = [[0]*w for i in range(h)]
q = int(input())
Qlis = [[int(i)-1 for i in input().split()] for j in range(q)]
for Q in Qlis:
    if Q[0] == 0:
        _,x,y = Q
        color[x][y] = 1
        for i,j in ((1,0),(0,1),(-1,0),(0,-1)):
            nx = x+i
            ny = y+j
            if 0 <= nx < h and 0 <= ny < w and color[nx][ny]:
                uf.union(x*w+y, nx*w+ny)
    else:
        _, ax,ay,bx,by = Q
        print("Yes" if uf.same(ax*w+ay, bx*w+by) and color[ax][ay] and color[bx][by]  else "No")

