n,q = map(int,input().split())
mod = 10**9+7
Q = [list(map(int,input().split())) for i in range(q)]

ans = 1
for i in range(60):
    count = 0
    for j in range(1<<n):
        ok = 1
        for x,y,z,w in Q:
            x,y,z = x-1,y-1,z-1
            if w >> i & 1:
                if (j >> x & 1) or  (j >> y & 1) or (j >> z & 1):
                    continue
                else:
                    ok = 0
                    break
            else:
                if (j >> x & 1) or  (j >> y & 1) or (j >> z & 1):
                    ok = 0
                    break
        if ok:
            count += 1
    ans *= count
    ans %= mod
print(ans)