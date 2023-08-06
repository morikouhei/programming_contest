a,b = map(int,input().split())
l = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    for j in range(3):
        if l[i][j] != a:
            continue
        for dx,dy in [[0,1],[0,-1]]:
            ni,nj = i+dx,j+dy
            if 0 <= ni < 3 and 0 <= nj < 3 and l[ni][nj] == b:
                print("Yes")
                exit()
print("No")