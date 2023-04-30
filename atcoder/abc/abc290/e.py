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
A = list(map(int,input().split()))

e = [[] for i in range(n+1)]
for i,a in enumerate(A):
    e[a].append(i)


count = 0
bit_num = BIT(n+5)
bit_sum = BIT(n+5)
ans = 0
for x in e:
    size = 0

    for ind in x:
        size += 1
        bit_num.add(ind,1)
        bit_sum.add(ind,n-ind)
    

    for ind in x:
        r = n-1-ind
        num = 0
        # print(ind,r)
        
        if r > ind:
            # ans += (r-ind)*(ind+1)
            num = bit_num.sum(r+1)-1
            ans += (r-ind-num)*(ind+1)
            count += (ind+1)*num
            # print("a",(ind+1)*num,num)

        dif = n-max(r,ind)-1

        # ans += dif*(dif-1)//2
        other = size-num-1
        # print(other,size)
        num = bit_sum.sum(n+1)-bit_sum.sum(max(ind+1,r+1))
        ans += dif*(dif+1)//2-num

        count += n*other-num
        # print(other,size,num,count)
        bit_num.add(ind,-1)
        bit_sum.add(ind,ind-n)
        size -= 1
print(ans)
# ans = ans -count
# print(ans)
