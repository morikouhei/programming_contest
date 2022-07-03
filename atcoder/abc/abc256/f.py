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


n,q = map(int,input().split())
A = list(map(int,input().split()))
Q = [list(map(int,input().split())) for i in range(q)]

bit0 = BIT(n+5)
bit1 = BIT(n+5)
bit2 = BIT(n+5)

inv2 = pow(2,mod-2,mod)
def add(x,v):
    bit0.add(x,v)
    bit1.add(x,v*x)
    bit2.add(x,v*x*x)

def get(x):
    ans = bit0.sum(x+1) * (1+x)*(2+x)%mod
    ans += bit1.sum(x+1) * (-2*x-3) + bit2.sum(x+1) 
    ans %= mod 
    ans *= inv2
    return ans%mod

for i,a in enumerate(A,1):
    add(i,a)

for q in Q:
    if q[0] == 1:
        _,x,v = q
        dx = v-A[x-1]
        A[x-1] = v
        add(x,dx)
    else:
        print(get(q[1]))