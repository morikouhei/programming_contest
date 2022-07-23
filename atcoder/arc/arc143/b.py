mod = 10**9+7

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


n,k = map(int,input().split())
A = list(map(int,input().split()))
S = input()

dic = {a:i for i,a in enumerate(sorted(set(A)),1)}
l = len(dic+5)

dp = [BIT(l) for i in range(k+1)]

for i,a in enumerate(A):
    s = dic[a]
    for j in range(min(i+1,k+1)):
        if j == 0:
            dp[0].add(s,1)
            continue
        if S[j-1] == "<":
            x = dp[j-1].sum(s)
            dp[j].add(s,x)
        else:
            x = dp[j-1].sum(l)-dp[j-1].sum