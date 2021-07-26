A = list(map(int,input().split()))

ans = max(A)*3-sum(A)

ans2 = 0
A2 = A[:]
if A2[0] > A2[1]:
    ans2 += A2[0]-A2[1]
    A2[1] = A2[0]
if A2[1]-A2[0] >= A2[2]-A2[1]:
    ans2 += A2[0]+(A2[1]-A2[0])*2-A2[2]
else:
    ans2 += (A2[2]-A2[0]+1)//2-(A2[1]-A2[0])+(A2[2]-A2[0])%2
A = A[::-1]

ans3 = 0
if A[0] > A[1]:
    ans3 += A[0]-A[1]
    A[1] = A[0]
if A[1]-A[0] >= A[2]-A[1]:
    ans3 += A[0]+(A[1]-A[0])*2-A[2]
else:
    ans3 += (A[2]-A[0]+1)//2-(A[1]-A[0])+(A[2]-A[0])%2
print(min(ans,ans2,ans3))