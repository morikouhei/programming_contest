n,m = map(int,input().split())
A = [[0]*m for i in range(n)]
for i in range(n):
    t = int(input())
    a = [int(x)-1 for x in input().split()]
    for j in a:
        A[i][j] = 1
S = list(map(int,input().split()))
mod = 998244353
pos = 0
for i in range(m):
    upd = False
    for j in range(pos,n):
        if A[j][i]:
            A[j],A[pos] = A[pos],A[j]
            upd = True
            break
    if upd == False:
        continue
    for j in range(n):
        if j == pos:
            continue
        if A[j][i] == 0:
            continue
        for k in range(m):
            A[j][k] ^= A[pos][k]
    if S[i]:
        for k in range(m):
            S[k] ^= A[pos][k]
    pos += 1

ans = 1
if 1 in S:
    ans = 0
ans *= pow(2,n-pos,mod)
print(ans)