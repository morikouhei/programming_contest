h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]
for i in range(h):
    for j in range(w):
        for k in range(i):
            for t in range(j):
                if A[k][t]+A[i][j] > A[i][t]+A[k][j]:
                    print("No")
                    exit()
print("Yes")