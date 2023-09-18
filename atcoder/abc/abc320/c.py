m = int(input())
ans = -1
S = [list(map(int,input())) for i in range(3)]
inf = 10**10
dp = [[0]*8 for i in range(10)]
print(S)
for i in range(10):
    dp[i][0] = 1
for i in range(3*m):

    ndp = [[0]*8 for j in range(10)]
    for j in range(10):
        for k in range(8):
            ndp[j][k] |= dp[j][k]

    for x in range(3):
        s = S[x][i%m]
        for b in range(8):
            if dp[s][b] == 0:
                continue
            print(x,s,b,i,b|(1<<x))
            ndp[s][b|(1<<x)] = 1
    
    dp = ndp
    print(dp[8])
    for j in range(10):
        if dp[j][7]:

            print(i+1)
            exit()
print(-1)