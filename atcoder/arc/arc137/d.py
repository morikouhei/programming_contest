n,m = map(int,input().split())
A = [0]*(1<<20)
for i,a in enumerate(list(map(int,input().split()))[::-1]):
    A[i] = a

for i in range(30):
    for j in range(1<<20):
        if j >> i & 1:
            A[j] ^= A[j^1<<i]

print(*A[-m:][::-1])