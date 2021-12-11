from collections import deque

H,W,h1,w1,h2,w2 = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
h2 = min(h1,h2)
w2 = min(w1,w2)
cumA = [[0]*(W+1) for i in range(H+1)]
for i in range(H):
    for j in range(W):
        cumA[i+1][j+1] = A[i][j]+cumA[i][j+1]+cumA[i+1][j]-cumA[i][j]

dp = [[] for i in range(H)]
for i in range(H-h2+1):

    q = deque([])
    for j in range(W-w2+1):
        count = cumA[i+h2][j+w2]-cumA[i][j+w2]-cumA[i+h2][j]+cumA[i][j]
        while q and q[-1][1] <= count:
            q.pop()
        q.append([j,count])
        if j >= w1-w2:
            dp[i].append(q[0][1])
        if q[0][0] <= j-(w1-w2):
            q.popleft()

ans = 0
for j in range(W-w1+1):

    q = deque([])
    for i in range(H-h2+1):
        count = dp[i][j]
        while q and q[-1][1] <= count:
                q.pop()
        q.append([i,count])
        if i >= h1-h2:
            ni = i-(h1-h2)
            count = cumA[ni+h1][j+w1]-cumA[ni][j+w1]-cumA[ni+h1][j]+cumA[ni][j]
            ans = max(ans,count-q[0][1])
        if q[0][0] <= i-(h1-h2):
            q.popleft()
print(ans)