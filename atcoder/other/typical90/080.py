n,d = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(1<<n):
    base = 0
    c = 0
    for j in range(n):
        if i >> j & 1:
            base |= A[j]
            c ^= 1
    ans += (-1)**(c)*pow(2,d-bin(base).count("1"))
print(ans)