n = int(input())
A = list(map(int,input().split()))
rem = A[-1]
for i in range(n-1):
    if A[i+1] < A[i]:
        rem = A[i]
        break

ans = []
for a in A:
    if a != rem:
        ans.append(a)

print(*ans)