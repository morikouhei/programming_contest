m = int(input())
ans = -1
S = [list(map(int,input())) for i in range(3)]
dp = [[0]*8 for i in range(10)]
for i in range(10):
    dp[i][0] = 1
for i in range(3*m):

    ndp = set()

    for x in range(3):
        s = S[x][i%m]
        for b in range(8):
            if dp[s][b] == 0:
                continue
            ndp.add((s,b|1<<x))
    
    for s,b in ndp:
        dp[s][b] |= 1
    for j in range(10):
        if dp[j][7]:
            print(i)
            exit()
print(-1)