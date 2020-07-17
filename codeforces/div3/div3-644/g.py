t = int(input())
for _ in range(t):
    n,m,a,b = map(int,input().split())
    
    if n*a != m*b:
        print("NO")
        continue
    ans = [[0]*m for i in range(n)]
    for i in range(a):
        ans[0][i] = 1
    for i in range(1,n):
        for j in range(m):
            if ans[i-1][j] == 1:
                ans[i][(j+a)%m] = 1
    print("YES")
    for i in ans:
        print(*i,sep="")