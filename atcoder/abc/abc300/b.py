h,w = map(int,input().split())
A = [input() for i in range(h)]
B = [input() for i in range(h)]

sA = [["."]*(2*w) for i in range(2*h)]
for i in range(2*h):
    for j in range(2*w):
        sA[i][j] = A[i%h][j%w]


for i in range(h):
    for j in range(w):

        ok = 1
        for x in range(h):
            for y in range(w):
                if B[x][y] != sA[i+x][j+y]:
                    ok = 0
        
        if ok:
            print("Yes")
            exit()
print("No")