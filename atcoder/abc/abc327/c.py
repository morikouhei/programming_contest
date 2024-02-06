A = [list(map(int,input().split())) for i in range(9)]

ok = 1

for i in range(9):

    if len(set(A[i])) != 9:
        ok = 0

for i in range(9):
    l = []
    for j in range(9):
        l.append(A[j][i])
    
    if len(set(l)) != 9:
        ok = 0

for i in range(3):

    for j in range(3):

        l = []

        for x in range(3):
            for y in range(3):
                l.append(A[i*3+x][j*3+y])
        
        if len(set(l)) != 9:
            ok = 0

print("Yes" if ok else "No")