n,m,p = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

ans = 0

pos = 0
b = 0
for a in A[::-1]:
    while pos < m and B[pos]+a <= p:
        b += B[pos]
        pos += 1
    ans += b + a*pos + p * (m-pos)
print(ans)