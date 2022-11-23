n = int(input())

S = [input() for i in range(n)]


dp = [[0]*n for i in range(1<<n)]

### 1 win First
### 0 win Second
for i in range(1<<n)[::-1]:
    for j in range(n):
        if not i >> j & 1:
            continue
        

        s = S[j][-1]
        t = bin(i).count("1")%2
        find = 0
        win = 0

        for k in range(n):
            if i >> k & 1 or S[k][0] != s:
                continue
            find = 1
            if t == 0: ###first turn
                if dp[i|1<<k][k]:
                    win = 1
            else:
                if dp[i|1<<k][k] == 0:
                    win = 1
        
        if find:
            if win:
                dp[i][j] = t^1
            else:
                dp[i][j] = t
        else:
            dp[i][j] = t



for i in range(n):
    if dp[1<<i][i]:
        print("First")
        exit()
print("Second")