class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
 
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
        ri = 1
        while ri<n:
            ri = ri<<1
        while ri > 0:
            if le+ri < n and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri = ri >> 1
        return le+1

n = 10
bit = BIT(n)
for i in range(10):
    bit.add(i,i)
print(bit.bsearch(34))