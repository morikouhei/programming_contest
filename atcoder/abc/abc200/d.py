n = int(input())
A = list(map(int,input().split()))

dp = [[[-1]*(200) for i in range(n+1)] for j in range(n+1)]
dp[0][0][0] = 0

def ans(i,j,k,last):
    print("Yes")

    X = []
    Y = []
    xi = i
    xj = j
    xk = k
    while xi and xj:
        #print(xi,xj,xk,X)
        if dp[xi][xj][xk] == -1:
            xi -= 1
        else:
            X.append(dp[xi][xj][xk])
            xk = (xk-A[X[-1]-1]%200)%200
            xj -= 1
            xi -= 1
        #print(xi,xj,xk,X)
    Y.append(last)
    yi = i-1
    yj = j-1
    yk = (k-A[Y[-1]-1]%200)%200
    while yi and yj:
        #print(yi,yj,yk,Y)
        if dp[yi][yj][yk] == -1:
            yi -= 1
        else:
            Y.append(dp[yi][yj][yk])
            yk = (yk-A[Y[-1]-1]%200)%200
            yj -= 1
            yi -= 1
        #print(yi,yj,yk,Y)
    if X[-1] == 0:
        X.pop()
    if Y[-1] == 0:
        Y.pop()
    X.sort()
    Y.sort()
    print(len(X),*X)
    print(len(Y),*Y)
    exit()

def ans2(i,j,k):
    X = []
    Y = []
    xi = i
    xj = j
    xk = k
    while xi:
        if dp[xi][xj][xk] == -1:
            xi -= 1
        else:
            X.append(dp[xi][xj][xk])
            xk = (xk-A[X[-1]-1]%200)%200
            xj -= 1
            xi -= 1
    if X[-1] == 0:
        X.pop()
    X.sort()
    print(len(X),*X)

for i,a in enumerate(A):
    x = a%200
    for j in range(n):
        for k in range(200):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = dp[i][j][k]            

            if dp[i][j+1][(k+x)%200] != -1:
                ans(i+1,j+1,(k+x)%200,i+1)

            dp[i+1][j+1][(k+x)%200] = i+1

for i in range(200):
    for j in range(1,n+1):
        for k in range(1,j):
            if dp[-1][j][i] != -1 and dp[-1][k][i] != -1:
                print("Yes")
                ans2(n,j,i)
                ans2(n,k,i)
                exit()
print("No")