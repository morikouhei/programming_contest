h,w = map(int,input().split())
C = [input() for i in range(h)]
mod = 10**9+7


l1 = [0]
l2 = []
for i in range(w+1):
    nl1 = []
    nl2 = []
    for j in l1:
        nl1.append(j*2)
        if j >> (w-1):
            continue
        if j%2:
            nl2.append(j*2+1)
        else:
            nl1.append(j*2+1)
    for j in l2:
        nl2.append(j*2)
        if j%2:
            continue
        nl2.append(j*2+1)
    l1 = nl1
    l2 = nl2
l = sorted(l1+l2)
dic = {x:i for i,x in enumerate(l)}
dic2 = {i:x for i,x in enumerate(l)}
le = len(l)
dp = [0]*le
dp[0] = 1
M = 1<<(w+1)
to0 = [0]*le
to1 = [0]*le
for i in range(le):
    num = dic2[i]
    to0[i] = dic[num*2%M]
    if num*2%M+1 in dic:
        to1[i] = dic[num*2%M+1]
def add_king(x,j,t1):
    if x >> w-1 & 1:
        return 
    if j != 0 and x >> 0 & 1:
        return
    if j != 0 and x >> w & 1:
        return
    if j != w-1 and x >> (w-2) & 1:
        return 
    ndp[t1] += dp[dic[x]]
    ndp[t1] %= mod


for i in range(h):
    for j in range(w):
        ndp = [0]*le
        for k in range(le):
            if dp[k] == 0:
                continue
            num,t0,t1 = dic2[k],to0[k],to1[k]
            if C[i][j] == ".":
                add_king(num,j,t1)
            ndp[t0] += dp[k]
            ndp[t0] %= mod
        dp = ndp

ans = 0
for i in dp:
    ans += i
    ans %= mod
print(ans)