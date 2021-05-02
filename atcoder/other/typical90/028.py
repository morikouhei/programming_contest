n = int(input())
M = 1005
count = [[0]*M for i in range(M)]
for i in range(n):
    lx,ly,rx,ry = map(int,input().split())
    count[lx][ly] += 1
    count[rx][ry] += 1
    count[lx][ry] -= 1
    count[rx][ly] -= 1

for i in range(M):
    for j in range(M-1):
        count[i][j+1] += count[i][j]

for i in range(M):
    for j in range(M-1):
        count[j+1][i] += count[j][i]

ans = [0]*(n+1)
for i in range(M):
    for j in range(M):
        ans[count[i][j]] += 1

for i in ans[1:]:
    print(i)