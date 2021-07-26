h,w,c = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

ans = 10**20
for _ in range(2):
    cost = [[10**20]*w for i in range(h)]

    for i in range(h):
        for j in range(w):
            cost[i][j] = min(cost[i][j],cost[i-1][j])
            cost[i][j] = min(cost[i][j],cost[i][j-1])
            ans = min(ans,A[i][j]+c*(i+j)+cost[i][j])
            cost[i][j] = min(cost[i][j],A[i][j]-c*(i+j))

    nA = []
    for i in range(h)[::-1]:
        nA.append(A[i])
    A = nA
print(ans)
