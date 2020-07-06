N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))

mod = 10**9+7
ans = 1
mi = []
pl = []
for a in A:
    if a < 0:
        mi.append(a)
    else:
        pl.append(a)

if N == K:
    for a in A:
        ans *= a
        ans %= mod
    print(ans)
    exit()
if pl == []:
    if K%2:
        for k in range(K):
            ans *= mi[-1-k]
            ans %= mod
    else:
        for k in range(K):
            ans *= mi[k]
            ans %= mod
    print(ans)
    exit()

pl = pl[::-1]

ip = 0
im = 0
if K % 2:
    ans = pl[0]
    ip += 1
    K -= 1

while K > 0:
    check = True
    if ip + 2 <= len(pl):
        x = pl[ip]*pl[ip+1]
    else:
        x = 1
    if im + 2 <= len(mi):
        y = mi[im]*mi[im+1]
    else:
        check = False
        y = 1

    if x >= y or check == False:
        ans *= x
        ans %= mod
        ip += 2
    else:
        ans *= y
        ans %= mod
        im += 2
    K -= 2
print(ans)
    
