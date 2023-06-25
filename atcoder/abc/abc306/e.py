import sys
input = sys.stdin.readline
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

n,k,q = map(int,input().split())

XY = [list(map(int,input().split())) for i in range(q)]

s = set()
s.add(0)
for _,y in XY:
    s.add(-y)

le = len(s)
s = sorted(s)
dic = {x:i for i,x in enumerate(s)}
rdic = {i:x for i,x in enumerate(s)}
bit_sum = BIT(le+1)
bit_num = BIT(le+1)
bit_num.add(le-1,n)
A = [0]*n
for x,y in XY:
    x -= 1
    y *= -1
    ind = dic[y]

    bind = dic[A[x]]

    bit_num.add(bind,-1)
    bit_sum.add(bind,-A[x])

    A[x] = y
    bit_num.add(ind,1)
    bit_sum.add(ind,y)

    pos = bit_num.bsearch(k)
    num = bit_num.sum(pos)

    score = bit_sum.sum(pos)

    if num > k:
        ny = rdic[pos-1]
        score -= ny * (num-k)
    print(-score)
