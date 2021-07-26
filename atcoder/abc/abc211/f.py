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

n = int(input())
M = 10**5+5
event = [[] for i in range(M)]
XY = []
for _ in range(n):
    m = int(input())
    l = list(map(int,input().split()))
    xy = [[l[i],l[i+1]] for i in range(0,2*m,2)]
    ind = 0
    x,y = xy[0]
    for i,(nx,ny) in enumerate(xy):
        if nx > x or (nx == x and y > ny):
            continue
        ind = i
        x = nx
        y = ny
    xy = xy[ind:]+xy[:ind]
    if xy[0][0] != xy[1][0]:
        xy[1:] = xy[1:][::-1]

    for i in range(0,m,2):
        x,y = xy[i]
        _,ny = xy[i+1]
        d = 1
        if y < ny:
            d = -1
            y,ny = ny,y
        event[x].append((y,ny,d))
q = int(input())
query = [[] for i in range(M)]
for i in range(q):
    x,y = map(int,input().split())
    query[x].append((y,i))

bit = BIT(M)
ans = [0]*q

for i in range(M):
    for y,ny,d in event[i]:
        bit.add(ny,d)
        bit.add(y,-d)
    for y,ind in query[i]:
        ans[ind] = bit.sum(y+1)
for i in ans:
    print(i)