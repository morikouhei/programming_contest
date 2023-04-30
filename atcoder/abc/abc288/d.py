n,k = map(int,input().split())
A = list(map(int,input().split()))
q = int(input())
LR = [list(map(int,input().split())) for i in range(q)]

accum = [[0]*(n+1) for i in range(k)]
for i,a in enumerate(A):
    accum[i%k][i+1] = a

for i in range(k):
    for j in range(n):
        accum[i][j+1] += accum[i][j]

for l,r in LR:
    count = [accum[i][r]-accum[i][l-1] for i in range(k)]
    print("Yes" if len(set(count)) == 1 else "No") 