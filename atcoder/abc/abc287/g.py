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


n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
q = int(input())
Q = [list(map(int,input().split())) for i in range(q)]

s = set([a for a,_ in AB])
for q in Q:
    if q[0] == 1:
        s.add(q[2])
s.add(0)
point = [0]*n
cards = [0]*n
s = sorted(s,reverse=True)
le = len(s)
dic = {x:i for i,x in enumerate(s)}
bit_num = BIT(le+1)
bit_sum = BIT(le+1)

def add_bit(ind,a,b):
    bef_a = point[ind]
    bef_b = cards[ind]

    bef_ind = dic[bef_a]
    bit_num.add(bef_ind,-bef_b)
    bit_sum.add(bef_ind,-bef_a*bef_b)

    aft_ind = dic[a]
    bit_num.add(aft_ind,b)
    bit_sum.add(aft_ind,a*b)

    point[ind] = a
    cards[ind] = b

for i,(a,b) in enumerate(AB):
    add_bit(i,a,b)

for q in Q:
    if q[0] == 1:
        x,y = q[1:]
        x -= 1
        add_bit(x,y,cards[x])

    elif q[0] == 2:
        x,y = q[1:]
        x -= 1
        add_bit(x,point[x],y)

    else:
        x = q[1]
        rind = bit_num.bsearch(x)
        if rind > le+1:
            print(-1)
        else:
            ans = bit_sum.sum(rind-1)
            dif = x-bit_num.sum(rind-1)
            ans += dif * s[rind-1]
            print(ans)