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
A = [list(map(int,input().split())) for i in range(n)]

bit = BIT(n)
bit.build([1]*n)
nums = n
inds = [1]*n
sA = []
for i in range(n):
    for a in A[i]:
        sA.append([a,i])

ans = 0
sA.sort()

for a,ind in sA:
    
    base = nums - bit.sum(ind+1)

    ans += base + (inds[ind]-1)*(n-1-ind)
    inds[ind] += 1
    bit.add(ind,1)
    nums += 1
print(ans)