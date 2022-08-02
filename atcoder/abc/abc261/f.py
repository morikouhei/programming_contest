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

n = int(input())
C = list(map(int,input().split()))
X = list(map(int,input().split()))

col = [[] for i in range(n+1)]
for i,c in enumerate(C):
    col[c].append(i)


dic = {}
bits = []
for i in range(n+1):
    l = len(col[i])
    bit = BIT(l+5)
    for j,ind in enumerate(col[i]):
        dic[ind] = j+1
        bit.add(j+1,1)
    bits.append(bit)

sX = [[x,i] for i,x in enumerate(X)]
sX.sort()

bit = BIT(n+5)
ans = 0

left = [[] for i in range(n+1)]
for num,(x,ind) in enumerate(sX):

    sind = dic[ind]
    c = C[ind]
    ans += ind -  bit.sum(ind)
    # print(num,x,ind,c)
    # print(ind -  bit.sum(ind))
    ans -= bits[c].sum(sind)
    bits[c].add(sind,-1)

    bit.add(ind,1)

print(ans)
