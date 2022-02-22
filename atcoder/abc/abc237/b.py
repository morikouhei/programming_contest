h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]
B = [[0]*h for i in range(w)]
for i in range(h):
    for j in range(w):
        B[j][i] = A[i][j]

for i in B:
    print(*i)