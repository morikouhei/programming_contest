n = int(input())
L = [list(map(int,input().split())) for i in range(3)]

ans = 0
count = [[0]*46 for i in range(3)]
for i,l in enumerate(L):
    for j in l:
        count[i][j%46] += 1

for i in range(46):
    for j in range(46):
        k = (-i-j)%46
        ans += count[0][i]*count[1][j]*count[2][k]
print(ans)