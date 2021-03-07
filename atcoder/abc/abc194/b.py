n = int(input())
ans = 10**10
ab = [list(map(int,input().split())) for i in range(n)]

A = []
B = []
for i, (a,b) in enumerate(ab):
    A.append((a,i))
    B.append((b,i))
A.sort()
B.sort()
if A[0][1] != B[0][1]:
    ans = max(A[0][0],B[0][0])
else:
    ans = min(A[0][0] + B[0][0], max(A[0][0],B[1][0]),max(A[1][0],B[0][0]))
print(ans)