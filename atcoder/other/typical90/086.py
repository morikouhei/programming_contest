n,q = map(int,input().split())
mod = 10**9+7
Q = [list(map(int,input().split())) for i in range(q)]

ans = 1
for i in range(60):
    count = 0
    for j in range(1<<n):
        ok = 1
        for x,y,z,q in Q:

            if ((j >> x & 1) | (j >> y & 1) | (j >> z & 1)) == q>>i & 1:
                print(1)
                continue
            ok = 0
            break
        if ok:
            count += 1
    ans *= count
    ans %= mod
print(ans)