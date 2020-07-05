t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    l = [list(map(int,input().split())) for i in range(n)]
    d = [[0]*m for i in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    check = True
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if 0 <= i+dx[k] < n and 0 <= j+dy[k] < m:
                    d[i][j] += 1
            if l[i][j] > d[i][j]:
                check = False
                break
    if check:
        print("YES")
        for i in d:
            print(*i)
    else:
        print("NO")
                