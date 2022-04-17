from collections import deque

n = int(input())
A = list(map(int,input().split()))
M = 10**5+1
idx = [[] for i in range(M)]
for i,a in enumerate(A):
    idx[a].append(i)

e = [[] for i in range(n)]
for _ in range(n-1):
    u,v = [int(x)-1 for x in input().split()]
    e[u].append(v)
    e[v].append(u)

mod = 998244353


count = [0]*M
used = [0]*n
size = [0]*n
par = [-1]*n
for i in range(1,M)[::-1]:
    for g in range(i,M,i):
        for now in idx[g]:
            if used[now] == i:
                continue
            par[now] = -1
            topo = []
            used[now] = i
          
            q = deque([now])
            while q:
                v = q.pop()
                topo.append(v)
                size[v] = 0
                for nex in e[v]:
                    if used[nex] == i or A[nex]%i:
                        continue
                    used[nex] = i
                    par[nex] = v
                    q.append(nex)

            s = len(topo)
            # print(size)
            for v in topo[::-1]:
                size[v] += 1
                count[i] += (s-size[v])*size[v]
                count[i] %= mod
                if par[v] != -1:
                    size[par[v]] += size[v]
            count[i] += s*(s-1)//2
            count[i] %= mod
            # print(i,g,s,count[i],size)


ans = 0
for i in range(1,M)[::-1]:
    for g in range(i*2,M,i):
        count[i] -= count[g]
        count[i] %= mod
    ans += i*count[i]%mod
    ans %= mod
print(ans)
            