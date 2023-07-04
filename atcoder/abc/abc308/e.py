n = int(input())
A = list(map(int,input().split()))
S = input()
ans = 0
M = [[0,0,0] for i in range(n)]
for i,(a,s) in enumerate(zip(A,S)):
    if i:
        for j in range(3):
            M[i][j] += M[i-1][j]

    if s == "M":
        M[i][a] += 1

X = [[0,0,0] for i in range(n)]
for i in range(n)[::-1]:
    if i != n-1:
        for j in range(3):
            X[i][j] += X[i+1][j]
    
    s = S[i]
    a = A[i]
    if s == "X":
        X[i][a] += 1




for i,s in enumerate(S):
    if s != "E":
        continue

    a = A[i]
    for j,x in enumerate(M[i]):

        for k,y in enumerate(X[i]):

            s = (a,j,k)
            for t in range(4):
                if t not in s:
                    ans += x*y*t
                    break
print(ans)