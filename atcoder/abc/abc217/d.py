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

l,q = map(int,input().split())

s = set()
s.add(0)
s.add(l)
Q = [list(map(int,input().split())) for i in range(q)] 
for c,x in Q:
    s.add(x)
s = sorted(s)
dic = {x:i for i,x in enumerate(s)}
n = len(s)
bit = BIT(n)
for c,x in Q:
    if c == 1:
        ind = dic[x]
        bit.add(ind,1)
        continue
    num = bit.sum(dic[x])
    le = bit.bsearch(num)-1
    ri = bit.bsearch(num+1)-1
    if ri >= n:
        print(l-s[le])
    else:
        print(s[ri]-s[le])
