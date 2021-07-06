h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(h)]
B = [list(map(int,input().split())) for i in range(h)]
ans = 0
for i in range(h-1):
    for j in range(w-1):
        dif = B[i][j]-A[i][j]
        ans += abs(dif)
        A[i][j] += dif
        A[i+1][j] += dif
        A[i][j+1] += dif
        A[i+1][j+1] += dif

for i in range(h):
    if A[i][-1] != B[i][-1]:
        print("No")
        exit()
for i in range(w):
    if A[-1][i] != B[-1][i]:
        print("No")
        exit()
print("Yes")
print(ans)