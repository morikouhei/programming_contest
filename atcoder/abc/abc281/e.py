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

n,m,k = map(int,input().split())
A = list(map(int,input().split()))

sA = sorted(set(A))
comp = {x:i for i,x in enumerate(sA)}

ans = []

bit_sum = BIT(n+5)
bit_count = BIT(n+5)

for i,a in enumerate(A):
    ind = comp[a]
    bit_count.add(ind,1)
    bit_sum.add(ind,a)

    if i < m-1:
        continue


    pos = bit_count.bsearch(k)
    num = bit_count.sum(pos)
    count = bit_sum.sum(pos)
    if num > k:
        count -= (num-k)*sA[pos-1]
    ans.append(count)
    bef = A[i-m+1]
    bit_count.add(comp[bef],-1)
    bit_sum.add(comp[bef],-bef)

print(*ans)
