n,k = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
inf = 10**5
for i in range(n):
    for j in range(n):
        if A[i][j] == 0:
            A[i][j] = inf


for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][k]+A[k][j],A[i][j])


q = int(input())
for _ in range(q):
    s,t = [int(x)-1 for x in input().split()]
    s %= n
    t %= n
    ans = A[s][t]
    if ans == inf:
        ans = -1

    print(ans)
