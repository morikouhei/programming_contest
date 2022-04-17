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



n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))
AB = [[a,b] for a,b in zip(A,B)]
CD = [[c,d] for c,d in zip(C,D)]

AB.sort()
CD.sort()
s = set()
for _,b in AB:
    s.add(b)
for _,d in CD:
    s.add(d)

dic = {x:i+1 for i,x in enumerate(sorted(s))}
ma = len(s)+5
bit = BIT(len(s)+5)
now = 0
for c,d in CD:
    while now < n and AB[now][0] <= c:
        x = AB[now][1]
        bit.add(dic[x],1)
        now += 1
    ind = dic[d]
    num = bit.sum(ind+1)
    if num == 0:
        continue
    bind = bit.bsearch(num)
    bit.add(bind-1,-1)

if now == n and bit.sum(ma) == 0:
    print("Yes")
else:
    print("No")
