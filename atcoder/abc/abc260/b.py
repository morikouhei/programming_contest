n,x,y,z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = [0]*n
A1 = [[a,i] for i,a in enumerate(A)]
A1.sort(key=lambda x:(-x[0],x[1]))
for i in range(x):
    ans[A1[i][1]] = 1

B1 = []
for i in range(n):
    if ans[i]:
        continue
    B1.append([B[i],i])
B1.sort(key=lambda x:(-x[0],x[1]))
for i in range(y):
    ans[B1[i][1]] = 1

C = []
for i in range(n):
    if ans[i]:
        continue
    C.append([A[i]+B[i],i])

C.sort(key=lambda x:(-x[0],x[1]))

for i in range(z):
    ans[C[i][1]] = 1

for i in range(n):
    if ans[i]:
        print(i+1)