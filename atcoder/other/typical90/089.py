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

n,k = map(int,input().split())
n += 1
A = [0]+list(map(int,input().split()))
mod = 10**9+7
sA = sorted(list(set(A)))
dic = {x:i for i,x in enumerate(sA)}
bit = BIT(len(sA)+5)
lmost = [0]*n
now = n-1
cum = 0
for i in range(n)[::-1]:
    while now >= 0 and cum <= k:
        bit.add(dic[A[now]],1)
        cum += bit.sum(dic[A[now]])
        now -= 1
    lmost[i] = now
    bit.add(dic[A[i]],-1)
    cum -= (i-now-1)-bit.sum(dic[A[i]]+1)

dp = [0]*n
cumdp = [0]*n
dp[0] = 1
cumdp[0] = 1
for i in range(1,n):
    dp[i] = cumdp[i-1]-cumdp[lmost[i]]
    dp[i] %= mod
    cumdp[i] = cumdp[i-1]+dp[i]
    cumdp[i] %= mod
print(dp[-1])
