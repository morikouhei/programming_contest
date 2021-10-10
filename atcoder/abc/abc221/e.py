n = int(input())
A = list(map(int,input().split()))
mod = 998244353

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
                self.tree[j] %= mod

    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            s %= mod
            i -= i & -i
        return s
    # 0 index を 1 index に変更  転倒数を求めるなら1を足していく
    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            self.tree[i] %= mod
            i += i & -i

s = set(A)
dic = {x:i for i,x in enumerate(sorted(s))}
l = [1]
for i in range(n+5):
    l.append(l[-1]*2%mod)

count = [0]
for i in range(n+4):
    count.append(l[i])
bit = BIT(n+5)
bit.build(count)
ans = 0
sA = [[a,i] for i,a in enumerate(A)]
sA.sort()
for a,i in sA:
    ans += (bit.sum(n)-bit.sum(i+1))%mod*pow(l[i],mod-2,mod)%mod
    ans %= mod
    if i == 0:
        continue
    bit.add(i,-l[i-1])
print(ans)