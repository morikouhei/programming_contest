n = int(input())
A = list(map(int,input().split()))
mod = 998244353

e = [[] for i in range(n)]
for i,a in enumerate(A):
    if a == -1:
        continue
    a -= 1
    e[i].append(a)
    e[a].append(i)

vis = [0]*n
trees = []
cycle = 0
for i in range(n):
    if vis[i]:
        continue
    tree = 0
    q = [i]
    vis[i] = 1
    size = 0
    while q:
        now = q.pop()
        size += 1
        if A[now] == -1:
            tree = 1
        for nex in e[now]:
            if vis[nex]:
                continue
            vis[nex] = 1
            q.append(nex)
    
    if tree:
        trees.append(size)
    else:
        cycle += 1
print(trees,cycle)
m = len(trees)
dp = [0]*(m+1)
dp[0] = 1
for t in trees:
    for i in range(m)[::-1]:
        dp[i+1] += dp[i]*t%mod
        dp[i+1] %= mod

ans = cycle * pow(n,m,mod)
fact = 1
for i in range(1,m+1):
    ans += dp[i]*fact*pow(n,m-i,mod)
    ans %= mod
    fact *= i
    fact %= mod
print(ans)