t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(-1)
        continue
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][(i+j)%n] = (i+1)+(n*j)
    for i in ans:
        print(*i)