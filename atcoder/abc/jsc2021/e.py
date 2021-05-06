class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]

k = int(input())
s = input()
now = s
nk = k
while nk and now:
    now = now[:len(now)//2]
    nk -= 1
if nk or len(now) == 1:
    print("impossible")
    exit()
n = len(s)
uf = Unionfind(n)
base = [[i for i in range(n)]]
while k:
    for b in base:
        for i in range(len(b)//2):
            uf.union(b[i],b[-1-i])
    for i in range(len(base)-1):
        for j in range(len(base[0])):
            uf.union(base[i][j],base[i+1][j])
    nbase = []
    for b in base:
        l,r = b[:len(b)//2],b[-(len(b)-1)//2:]
        nbase.append(l)
        nbase.append(r)
    base = nbase
    k -= 1

dic = {}
for i in range(n):
    p = uf.find(i)
    if p in dic:
        dic[p][ord(s[i])-ord("a")] += 1
    else:
        dic[p] = [0]*26
        dic[p][ord(s[i])-ord("a")] += 1

ans = 0
s = set(base[0])

for i in range(n):
    if uf.find(i) == i:
        if i in s:
            continue
        ans += sum(dic[i])-max(dic[i])
need = 0
cand = []
for i in base[0]:
    p = uf.find(i)
    need += sum(dic[p])-max(dic[p])
    cand.append(dic[p].index(max(dic[p])))
if cand == [] or cand != cand[::-1]:
    print(ans+need)
    exit()

now = 10**10
for i in base[0]:
    if len(base[0])%2 and i == len(base[0])//2:
        continue
    p = uf.find(i)
    m = max(dic[p])
    ind = dic[p].index(m)
    su = sum(dic[p])
    for j in range(26):
        if j == ind:
            continue
        now = min(now,need+m-dic[p][j])
print(ans+now)