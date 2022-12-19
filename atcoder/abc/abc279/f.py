
class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
        self.id = [i for i in range(n)]
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
        bx,by = self.id[x],self.id[y]
        self.id[y] = bx
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


n,q = map(int,input().split())
box = [[i] for i in range(n+1)]
M = n+q+5

OP = [list(map(int,input().split())) for i in range(q)]
uf = Unionfind(M)
used = n
for op in OP:
    if op[0] == 1:
        _,x,y = op

        if box[x]:
            if box[y]:
                xx = box[x][0]
                yy = box[y].pop()
                
                uf.union(xx,yy)
        else:
            if box[y]:
                yy = box[y].pop()
                p = uf.find(yy)
                uf.id[p] = x
                box[x].append(yy)
    
    elif op[0] == 2:
        used += 1
        x = op[1]
        uf.id[used] = x
        if box[x]:
            uf.union(box[x][0],used)
        else:
            box[x].append(used)
    
    else:
        x = op[1]
        p = uf.find(x)
        print(uf.id[p])