n = int(input())
W = list(map(int,input().split()))
B = list(map(int,input().split()))

grundy = [[0]*(1555) for i in range(55)]
for i in range(51):
    for j in range(1501):
        mex = [0]*1505
        if i > 0:
            mex[grundy[i-1][j+i]] = 1
        if j > 1:
            for k in range(1,j//2+1):
                mex[grundy[i][j-k]] = 1
        for k in range(1501):
            if mex[k]:
                continue
            grundy[i][j] = k
            break

ans = 0
for w,b in zip(W,B):
    ans ^= grundy[w][b]

if ans:
    print("First")
else:
    print("Second")