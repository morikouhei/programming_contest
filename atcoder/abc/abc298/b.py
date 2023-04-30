n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
B = [list(map(int,input().split())) for i in range(n)]

for _ in range(4):

    check = 1
    for i in range(n):
        for j in range(n):
            if A[i][j] and B[i][j] == 0:
                check = 0
    
    if check:
        print("Yes")
        exit()
    
    nA = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            nA[n-1-j][i] = A[i][j]

    A = nA
print("No")