n = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(n):
    x = 0
    for j in range(7):
        x += A[i*7+j]
    ans.append(x)

print(*ans)