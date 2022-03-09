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

q = int(input())
Q = [list(map(int,input().split())) for i in range(q)]
s = set()
ans = []
for l in Q:
    s.add(l[1])

s = sorted(s)
l = len(s)
dic = {x:i+1 for i,x in enumerate(s)}
rdic = {i+1:x for i,x in enumerate(s)}

bit = BIT(len(s)+5)
su = 0
for q in Q:
    if q[0] == 1:
        bit.add(dic[q[1]],1)
        su += 1
        continue
    t,x,k = q

    ind = dic[x]
    

    if t == 2:
        s = bit.sum(ind+1)
        if s < k:
            print(-1)
            continue
        ind = bit.bsearch(s-k+1)
        print(rdic[ind-1])

    else:
        s = bit.sum(ind)
        if su-s < k:
            print(-1)
            continue
        ind = bit.bsearch(s+k)
        print(rdic[ind-1])