class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
 
    def build(self, list):
        self.tree[1:] = list.copy()
        for i in range(self.size+1):
            j = i + (i & (-i))
            if j < self.size+1:
                self.tree[j] += self.tree[i]

    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s
    # 0 index を 1 index に変更  転倒数を求めるなら1を足していく
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # 総和がx以上になる位置のindex をbinary search
    def bsearch(self,x):
        le = 0
        ri = 1<<(self.size.bit_length()-1)
        while ri > 0:
            if le+ri <= self.size and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri >>= 1
        return le+1

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
n,k = map(int,input().split())
P = list(map(int,input().split()))

if k == 1:
    ans = [-1]*n
    for i,p in enumerate(P):
        ans[p-1] = i+1

    for i in ans:
        print(i)
    exit()
e = [[] for i in range(n+5)]

bit = BIT(n+5)
uf = Unionfind(n)
ans = [-1]*n

for i,p in enumerate(P):
    x = bit.sum(p)
    y = bit.bsearch(x+1)
    if y > n+1:
        bit.add(p,1)

    else:
        id = y-1
        uf.union(id-1,p-1)
        e[p-1].append(id-1)

        if uf.size(p-1) >= k:
            bit.add(id,-1)
            q = [p-1]
            ans[p-1] = i+1
            while q:
                now = q.pop()
                for nex in e[now]:
                    if ans[nex] != -1:
                        continue
                    ans[nex] = i+1
                    q.append(nex)

        else:
            bit.add(id,-1)
            bit.add(p,1)

for i in ans:
    print(i)