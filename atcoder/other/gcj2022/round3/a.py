import sys

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

def solve(n,k):
    L = list(map(int,input().split()))

    for _ in range(k):
        uf = Unionfind(n)
        for i,l in enumerate(L):
            uf.union(i,l-1)


        out = [0]*n
        num = 0
        col = {}
        for i in range(n):
            x = uf.find(i)
            if x in col:
                out[i] = col[x]
            else:
                num += 1
                col[x] = num
                out[i] = num
        print(*out)
        sys.stdout.flush()

        end = int(input())
        if end == 1:
            return 1

        L = list(map(int,input().split()))
   
    return 1
    

                    

            

t,n,k = map(int,input().split())
for i in range(t):
    solve(n,k)

    
