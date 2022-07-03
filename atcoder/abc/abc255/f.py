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

    # 総和がx以上になる位置のindex をbinary search
    def bsearch(self,x):
        le = 0
        ri = 1<<(self.size.bit_length()-1)
        while ri > 0:
            if le+ri <= self.size and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri >>= 1
        return le+1

n = int(input())
P = list(map(int,input().split()))
I = list(map(int,input().split()))
if P[0] != 1:
    print(-1)
    exit()

ans = [[0]*2 for i in range(n)]

idx = [0]*(n+1)
for i,p in enumerate(I):
    idx[p] = i

bit = BIT(n+5)

for i,now in enumerate(P):
    if i:
        p = P[i-1]
        if idx[now] < idx[p]:
            if ans[p-1][0] != 0:
                print(-1)
                exit()
            ans[p-1][0] = now
            
        else:
            s = bit.sum(idx[now])
            if s == 0:
                print(-1)
                exit()
            l = bit.bsearch(s)-1
            pp = I[l]
            if ans[pp-1][1] != 0:
                print(-1)
                exit()
            ans[pp-1][1] = now


    bit.add(idx[now],1)




pre = []
ino = []
import sys
sys.setrecursionlimit(3*10**5)

def dfs1(x):
    pre.append(x)
    if ans[x-1][0] != 0:
        dfs1(ans[x-1][0])
    if ans[x-1][1] != 0:
        dfs1(ans[x-1][1])


dfs1(1)

def dfs2(x):
    if ans[x-1][0] != 0:
        dfs2(ans[x-1][0])
    ino.append(x)
    if ans[x-1][1] != 0:
        dfs2(ans[x-1][1])


dfs2(1)
if pre == P and ino == I:
    for i in ans:
        print(*i)

else:
    print(-1)