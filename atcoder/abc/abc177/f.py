import sys 
input = sys.stdin.readline
from heapq import heappop,heappush

class BIT:
    def __init__(self, n):
        self.tree = [1]*(n+1)
        self.size = len(self.tree)
        self.tree[0] = 0
 
    def build(self):
        for i in range(self.size):
            j = i + (i & (-i))
            if j < self.size:
                self.tree[j] += self.tree[i]
    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
    # 0 index を 1 index に変更  転倒数を求めるなら1を足していく
    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i

    # 総和がx以上になる位置のindex をbinary search
    def bsearch(self,x):
        le = 0
        ri = 1<<(self.size.bit_length()-1)
        while ri > 0:
            if le+ri < self.size and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri >>= 1
        return le+1

h,w = map(int,input().split())
bit = BIT(w+3)
bit.build()

q = [0]*(w)
dp = [0]*(w+3)
dp[0] = -1
rm_q = []

for i in range(h):
    a,b = map(int,input().split())
    for x in [a-1,b+1]:
        if x == 0 or x == w+1:
            continue
        if dp[x] != -1:
            continue
        k = bit.sum(x)
        if k >= 1:
            xl = bit.bsearch(k)
            dp[x] = dp[xl]+(x-xl)
            bit.add(x,1)
            heappush(q,dp[x])
    k = bit.sum(a-1)+1
    while True:
        x = bit.bsearch(k)
        if x > b:
            break
        bit.add(x,-1)
        heappush(rm_q, dp[x])
        dp[x] = -1
    while rm_q and rm_q[0] == q[0]:
        heappop(rm_q)
        heappop(q)
    if q == []:
        print(-1)
    else:
        print(q[0]+i+1)
    