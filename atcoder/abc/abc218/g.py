from collections import deque
class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
 
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


n = int(input())
A = list(map(int,input().split()))
sA = sorted(set(A))
dic = {s:i for i,s in enumerate(sA)}
dic2 = {i:s for i,s in enumerate(sA)}
e = [[] for i in range(n)]
size = [0]*n
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)
    size[u] += 1
    size[v] += 1

bit = BIT(len(dic)+5)
done = [0]*n
done[0] = 1
q = deque([~0,0])
count = 0
dp = [0]*n
while q:
    now = q.pop()
    if now >= 0:
        bit.add(dic[A[now]],1)
        count += 1
        if now > 0 and size[now] == 1:
            if count%2:
                dp[now] = dic2[bit.bsearch(count//2+1)-1]
            else:
                dp[now] = (dic2[bit.bsearch(count//2)-1]+dic2[bit.bsearch(count//2+1)-1])//2
        for nex in e[now]:
            if done[nex]:
                continue
            done[nex] = 1
            q.append(~nex)
            q.append(nex)
    
    else:
        now = ~now
        bit.add(dic[A[now]],-1)
        count -= 1

        if dp[now]:
            continue
        if count%2:
            cand = 10**10
            for nex in e[now]:
                if dp[nex]:
                    cand = min(cand,dp[nex])
        else:
            cand = 0
            for nex in e[now]:
                if dp[nex]:
                    cand = max(cand,dp[nex])
        dp[now] = cand
print(dp[0])