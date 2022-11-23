H,W,n,h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]

ans = [[0]*(W-w+1) for i in range(H-h+1)]

cum = [[0]*(W+1) for i in range(H+1)]
for i in range(1,n+1):

    count = 0
    for j in range(H):
        for k in range(W):
            if A[j][k] == i:
                cum[j+1][k+1] = 1
                count += 1
            else:
                cum[j+1][k+1] = 0

    
    for j in range(H+1):
        for k in range(W):
            cum[j][k+1] += cum[j][k]
    
    for j in range(W+1):
        for k in range(H):
            cum[k+1][j] += cum[k][j]


    for j in range(H-h+1):
        for k in range(W-w+1):
            a,b = j,k
            c,d = j+h,k+w

            if count > cum[c][d]+cum[a][b]-cum[c][b]-cum[a][d]:
                ans[j][k] += 1

for i in ans:
    print(*i)
