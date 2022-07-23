def popcount(n):
    c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
    c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
    c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
    c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
    c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
    c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
    return c

def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    
    return x & 0x7f
    
n = int(input())
A = [input() for i in range(n)]

size = (n+62)//63

binA = []
for i in range(n):
    lis = []
    for j in range(size):
        l = j*63
        r = min(n,(j+1)*63)
        lis.append(int(A[i][l:r],2))
    binA.append(lis)


ans = 0
for i in range(n):
    for j in range(i):
        if A[i][j] != "1":
            continue
        for k in range(size):
            ans += popcount(binA[i][k]&binA[j][k])
print(ans//3)