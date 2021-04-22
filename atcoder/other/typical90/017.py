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

n,m = map(int,input().split())
LR = [tuple(map(int,input().split())) for i in range(m)]
LR.sort()
ans = m*(m-1)//2
L = [0]*(n+1)
R = [0]*(n+1)
for l,r in LR:
    L[l] += 1
    R[r] += 1
cumR = [0]
for i in range(1,n+1):
    cumR.append(cumR[i-1]+R[i])
for l in L:
    ans -= l*(l-1)//2
for l,r in LR:
    ans -= cumR[l]

bit = BIT(n+5)
for l,r in LR:
    ans -= bit.sum(n+1)-bit.sum(r+1)
    bit.add(r,1)
print(ans)