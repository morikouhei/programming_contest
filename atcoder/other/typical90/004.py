h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]

hsum = [0]*w
wsum = [0]*h

for i,a in enumerate(A):
    wsum[i] = sum(a)

for i in range(w):
    count = 0
    for j in range(h):
        count += A[j][i]
    hsum[i] = count

B = [[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        B[i][j] = wsum[i]+hsum[j]-A[i][j]

for b in B:
    print(*b)