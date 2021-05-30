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


n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sA = []
sB = []
for i,a in enumerate(A):
    sA.append(a+i)
for i,b in enumerate(B):
    sB.append(b+i)

dic = {x:i for i,x in enumerate(sorted(list(set(sA))))}
L = [[] for i in range(n+5)]
for i in range(n)[::-1]:
    L[dic[sA[i]]].append(i)

bit = BIT(n+5)
ans = 0
for i,b in enumerate(sB):
    if b not in dic or L[dic[b]] == []:
        print(-1)
        exit()
    x = L[dic[b]].pop()
    count = bit.sum(x)
    dif = i-count
    ans += abs(i-x-dif)
    bit.add(x,1)
print(ans)

