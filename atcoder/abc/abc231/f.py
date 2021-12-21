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
AB = [[a,b] for a,b in zip(A,B)]
AB.sort()
sa = set()
for a in A:
    sa.add(a)
dica = {x:i for i,x in enumerate(sorted(sa))}
lis = [[] for i in range(len(sa))]
for a,b in AB:
    lis[dica[a]].append(b)
s = set()
s.add(0)
for b in B:
    s.add(b)

l = len(s)
dic = {x:i for i,x in enumerate(sorted(s))}

bit = BIT(l+1)

ans = 0
count = 0
for l in lis:
    for b in l:
        count += 1
        bit.add(dic[b],1)
    for b in l:
        ans += count-bit.sum(dic[b])

print(ans)