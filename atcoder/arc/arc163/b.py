n,m = map(int,input().split())

A = list(map(int,input().split()))

ans = 10**20

a0,a1 = A[0],A[1]
A = A[2:]
A.sort()

m -= 1
for i in range(n-2):
    if i+m >= n-2:
        break


    count = max(0,a0-A[i]) + max(0,A[i+m]-a1)

    ans = min(ans,count)
print(ans)
    