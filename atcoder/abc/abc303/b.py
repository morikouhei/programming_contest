n,m = map(int,input().split())
A = [list(map(int,input().split())) for i in range(m)]

nums = [[0]*n for i in range(n)]
for a in A:
    for x,y in zip(a,a[1:]):
        x,y = x-1,y-1
        nums[x][y] += 1
        nums[y][x] += 1

ans = 0
for i in range(n):
    for j in range(n):
        if i == j or nums[i][j]:
            continue
        ans += 1
print(ans//2)