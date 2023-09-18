n = int(input())
A = list(map(int,input().split()))
A.sort()
for a,na in zip(A,A[1:]):
    if a+1 < na:
        print(a+1)
        exit()