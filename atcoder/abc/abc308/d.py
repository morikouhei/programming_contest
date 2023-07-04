from collections import deque
h,w = map(int,input().split())
S = [input() for i in range(h)]
snuke = "snuke"
if S[0][0] != "s":
    print("No")
    exit()

dp = [[[0]*5 for i in range(w)] for j in range(h)]
dp[0][0][0] = 1

q = deque([[0,0,0]])
while q:

    i,j,d = q.popleft()

    ns = snuke[(d+1)%5]
    nd = (d+1)%5

    if i != h-1 and S[i+1][j] == ns and dp[i+1][j][nd] == 0:
        dp[i+1][j][nd] = 1
        q.append([i+1,j,nd])
    
    if j != w-1 and S[i][j+1] == ns and dp[i][j+1][nd] == 0:
        dp[i][j+1][nd] = 1
        q.append([i,j+1,nd])

    
    if i and S[i-1][j] == ns and dp[i-1][j][nd] == 0:
        dp[i-1][j][nd] = 1
        q.append([i-1,j,nd])
    
    if j and S[i][j-1] == ns and dp[i][j-1][nd] == 0:
        dp[i][j-1][nd] = 1
        q.append([i,j-1,nd])


print("Yes" if sum(dp[-1][-1]) else "No")