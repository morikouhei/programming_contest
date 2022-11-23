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


ans = 0
M = max(A)+5
bit = BIT(M)
bit2 = BIT(M)
all = 0
for i,a in enumerate(A,1):

    s = bit.sum(a)
    s2 = bit.sum(a+1)
    ans += (all-s) + (all-s2)
    ans %= mod
    s = bit2.sum(a)
    s2 = bit2.sum(a+1)
    ans += a * (s+s2+1) % mod
    ans %= mod

    all += a
    bit.add(a,a)
    bit2.add(a,1)
    invi = pow(i**2,mod-2,mod)
    print(ans*invi%mod)