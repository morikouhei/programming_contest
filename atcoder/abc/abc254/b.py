n = int(input())
A = []
for i in range(n):
    nA = []
    for j in range(i+1):
        if j == 0 or j == i:
            nA.append(1)
        else:
            nA.append(A[j]+A[j-1])
    A = nA
    print(*A)