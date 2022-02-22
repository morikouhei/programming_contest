n = int(input())
S = list(map(int,input().split()))
A = [0]*(n+2)
for j in range(3):
    mi = 0
    for i in range(j,n-1,3):
        dif = S[i]-S[i+1]
        A[i+3] = A[i]-dif
        mi = min(mi,A[i+3])
    if mi < 0:
        for i in range(j,n+2,3):
            A[i] -= mi

dif = S[0]-(A[0]+A[1]+A[2])
if dif < 0:
    print("No")
    exit()

for i in range(0,n+2,3):
    A[i] += dif

print("Yes")
print(*A)

