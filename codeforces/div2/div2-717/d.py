import sys
input = sys.stdin.readline

n,q = map(int,input().split())
A = list(map(int,input().split()))
Q = [list(map(int,input().split())) for i in range(q)]

M = 10**5
fact = [[] for i in range(M+1)]
for i in range(2,M+1):
    if fact[i] != []:
        continue
    for j in range(i,M+1,i):
        fact[j].append(i)

dp = [-1]*n
now = 0
dic = {} 
for i in range(n):
    while now < n:
        ok = 1
        for c in fact[A[now]]:
            if dic.get(c,0) > 0:
                ok = 0
                break
        if ok == 0:
            break
        for c in fact[A[now]]:
            dic[c] = dic.get(c,0)+1
        now += 1
    dp[i] = now
    for c in fact[A[i]]:
        dic[c] -= 1

db = [dp]
for i in range(20):
    ndp = [n]*n
    for j in range(n):
        if db[-1][j] >= n:
            break
        ndp[j] = db[-1][db[-1][j]]
    db.append(ndp)

for l,r in Q:
    l -= 1
    r -= 1
    ans = 1
    for i in range(20)[::-1]:
        if db[i][l] <= r:
            ans += 1<<i
            l = db[i][l]
    print(ans)