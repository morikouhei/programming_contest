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

n,m,q = map(int,input().split())

Q = [tuple(map(int,input().split())) for i in range(q)]

s = set()
s.add(0)
for i in range(q):
    s.add(Q[i][-1])

le = len(s)
dic = {num:i for i,num in enumerate(sorted(list(s)))}

ans = 0
bitA = BIT(le+1)
bitB = BIT(le+1)
bitAsum = BIT(le+1)
bitBsum = BIT(le+1)
A = [0]*n
B = [0]*m
bitA.add(0,n)
bitB.add(0,m)

for t,x,y in Q:
    if t == 1:
        bef = A[x-1]
        if bef == y:
            print(ans)
            continue
        if bef < y:
            r = bitB.sum(dic[y])
            l = bitB.sum(dic[bef])
            rsum = bitBsum.sum(dic[y])
            lsum = bitBsum.sum(dic[bef])
            ans += y*r-rsum+lsum-bef*l
            bitA.add(dic[y],1)
            bitAsum.add(dic[y],y)
            bitA.add(dic[bef],-1)
            bitAsum.add(dic[bef],-bef)
            A[x-1] = y
        else:
            r = bitB.sum(dic[bef])
            l = bitB.sum(dic[y])
            rsum = bitBsum.sum(dic[bef])
            lsum = bitBsum.sum(dic[y])
            ans -= bef*r-rsum+lsum-y*l
            bitA.add(dic[y],1)
            bitAsum.add(dic[y],y)
            bitA.add(dic[bef],-1)
            bitAsum.add(dic[bef],-bef)
            A[x-1] = y
    else:
        bef = B[x-1]
        if bef == y:
            print(ans)
        if bef < y:
            r = bitA.sum(dic[y])
            l = bitA.sum(dic[bef])
            rsum = bitAsum.sum(dic[y])
            lsum = bitAsum.sum(dic[bef])
            ans += y*r-rsum+lsum-bef*l
            bitB.add(dic[y],1)
            bitBsum.add(dic[y],y)
            bitB.add(dic[bef],-1)
            bitBsum.add(dic[bef],-bef)
            B[x-1] = y
        else:
            r = bitA.sum(dic[bef])
            
            l = bitA.sum(dic[y])
            rsum = bitAsum.sum(dic[bef])
            lsum = bitAsum.sum(dic[y])
            ans -= bef*r-rsum+lsum-y*l
            bitB.add(dic[y],1)
            bitBsum.add(dic[y],y)
            bitB.add(dic[bef],-1)
            bitBsum.add(dic[bef],-bef)
            B[x-1] = y

    print(ans)

