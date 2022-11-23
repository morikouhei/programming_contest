n,x,y = map(int,input().split())
C = input()
mod = 998244353
M = 24

def calc(A,B):
    ans = [[0]*M for i in range(M)]
    for i in range(M):
        for j in range(M):
            for k in range(M):
                ans[i][j] += A[i][k]*B[k][j]
                ans[i][j] %= mod
    return ans



base = [[0]*M for i in range(M)]
for i in range(M):
    base[i][i] = 1


A = [[0]*M for i in range(M)]

r = 1
inv = pow(100,mod-2,mod)
for c in C:
    if c == "T":
        r *= 100-x
    else:
        r *= 100-y
    r *= inv
    r %= mod
rinv = pow(1-r,mod-2,mod)

for i in range(M):
    for j in range(M):
        a = 1
        ## i 時から始めて j-1 時に次のアクセスが当たる
        turn = (j+24-i)%24
        if turn == 0:
            turn = 24
        for k in range(turn):

            if C[(i+k)%24] == "T":
                if k == turn-1:
                    a *= x
                else:
                    a *= 100-x
            else:
                if k == turn-1:
                    a *= y
                else:
                    a *= 100-y
            a *= inv
            a %= mod
        A[i][j] = a*rinv%mod

while n:
    if n & 1:
        base = calc(A,base)
    A = calc(A,A)
    n >>= 1

ans = 0
for i in range(24):
    p = base[0][i]
    if C[(i-1)%24] == "A":
        ans += p
        ans %= mod
print(ans)

    