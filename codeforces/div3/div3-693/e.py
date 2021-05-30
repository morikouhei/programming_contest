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

    def bsearch(self,x):
        le = 0
        ri = 1<<(self.size.bit_length()-1)
        while ri > 0:
            if le+ri <= self.size and self.tree[le+ri]<x:
                x -= self.tree[le+ri]
                le += ri
            ri >>= 1
        return le+1

def solve():
    n = int(input())
    L = []
    ans = [-1]*n
    s = set()
    for i in range(n):
        h,w = map(int,input().split())
        if h > w:
            h,w = w,h
        s.add(w)
        L.append((h,w,i))
    L.sort(key=lambda x: (x[0],-x[1]))
    dic = {x:i+1 for i,x in enumerate(sorted(list(s)))}
    
    le = len(s)
    bit = BIT(le+5)
    cand = [[] for i in range(le+5)]
    for i in range(n):
        h,w,ind = L[i]
        num = bit.sum(dic[w])
        if num:
            x = bit.bsearch(1)
            ans[ind] = cand[x-1][-1]+1
        bit.add(dic[w],1)
        cand[dic[w]].append(ind)
    return ans
    

t = int(input())
for _ in range(t):
    ans = solve()
    print(*ans)