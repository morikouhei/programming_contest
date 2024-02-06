n,c = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def popcnt3(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

difs = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        difs[i][j] = abs(A[i]-B[j])
inf = 1<<56
dp = [inf]*(1<<n)
dp[0] = -c

for bi in range(1<<n):
    num = bin(bi).count("1")
    # num = popcnt3(bi)
    for l in range(n):
        cost = c + dp[bi]
        bid = num
        mask = bi
        for r in range(l,n):
            if bi >> r & 1:
                break
            mask |= 1 << r
            cost += difs[r][bid]
            bid += 1
            if dp[mask] > cost:
                dp[mask] = cost

print(dp[-1])
