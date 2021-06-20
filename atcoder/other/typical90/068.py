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
q = int(input())
inf = 10**20
bitodd = BIT(n+5)
biteven = BIT(n+5)
bitodd.build([inf if i%2 else 0 for i in range(n+5)])
biteven.build([0 if i%2 else inf for i in range(n+5)])
num = [inf]*(n+5)
Q = [list(map(int,input().split())) for i in range(q)]
for t,x,y,v in Q:

    if t:
        odd = bitodd.sum(max(x,y))-bitodd.sum(min(x,y))
        even = biteven.sum(max(x,y))-biteven.sum(min(x,y))
        if abs(odd) >= inf or abs(even) >= inf:
            print("Ambiguous")
            continue
        dif = odd-even
        if x < y:
            if x%2 == 1 and y%2 == 1:
                ans = v-dif
            elif x%2 == 1 and y%2 == 0:
                ans = dif-v
            elif x%2 == 0 and y%2 == 1:
                ans = -dif-v
            else:
                ans = dif+v
        else:
            if x%2 == 1 and y%2 == 1:
                ans = v+dif
            elif x%2 == 0 and y%2 == 1:
                ans = -v+dif
            elif x%2 == 1 and y%2 == 0:
                ans = -v-dif
            else:
                ans = v-dif

        print(ans)

    else:
        bef = num[x]
        if x%2:
            bitodd.add(x,v-bef)
        else:
            biteven.add(x,v-bef)
        num[x] = v    