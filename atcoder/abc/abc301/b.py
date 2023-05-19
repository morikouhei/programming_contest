n = int(input())
A = list(map(int,input().split()))

ans = []
for a,na in zip(A,A[1:]):
    ans.append(a)
    if a < na:
        for j in range(a+1,na):
            ans.append(j)
    elif a > na:
        for j in range(a-1,na,-1):
            ans.append(j)
print(*ans)