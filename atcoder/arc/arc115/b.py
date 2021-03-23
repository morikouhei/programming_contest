n = int(input())
C = [list(map(int,input().split())) for i in range(n)]
dB = []
for i in range(n-1):
    num = C[0][i+1]-C[0][i]
    dB.append(num)
    for j in range(n):
        if C[j][i+1]-C[j][i] != num:
            print("No")
            exit()

dA = []
for i in range(n-1):
    num = C[i+1][0]-C[i][0]
    dA.append(num)
    for j in range(n):
        if C[i+1][j]-C[i][j] != num:
            print("No")
            exit()

A = [0]
for a in dA:
    A.append(A[-1]+a)
mi = min(A)
for i in range(n):
    A[i] -= mi

B= [0]
for b in dB:
    B.append(B[-1]+b)
dif = C[0][0]-A[0]
for i in range(n):
    B[i] += dif

for i in range(n):
    for j in range(n):
        if C[i][j] != A[i]+B[j]:
            print("No")
            exit()
print("Yes")
print(*A)
print(*B)
