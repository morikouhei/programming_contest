n = int(input())
A = [list(map(int,input())) for i in range(n)]
ans = 0

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
for i in range(n):
    for j in range(n):
        
        for d in range(8):
            count = 0
            x,y = i,j
            for k in range(n):
                count *= 10
                count += A[x%n][y%n]
                x += dx[d]
                y += dy[d]
            ans = max(ans,count)
print(ans)