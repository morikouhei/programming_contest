from bisect import bisect_left

n = int(input())
A = list(map(int,input().split()))
L = [0]*n
R = [0]*n

lis = []
m = 0
for i in range(n):
    if lis == []:
        m += 1
        lis.append(A[i])
    else:
        ind = bisect_left(lis,A[i])
        if ind == m:
            m += 1
            lis.append(A[i])
        else:
            lis[ind] = A[i]
    L[i] = m 

lis = []
m = 0
for i in range(n)[::-1]:
    if lis == []:
        m += 1
        lis.append(A[i])
    else:
        ind = bisect_left(lis,A[i])
        if ind == m:
            m += 1
            lis.append(A[i])
        else:
            lis[ind] = A[i]
    R[i] = m 

ans = 0
for i in range(n):
    ans = max(ans,L[i]+R[i]-1)
print(ans)