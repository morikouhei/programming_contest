n = int(input())
S = input()
A = list(map(int,input().split()))

m = 10**5
for a,na in zip(A,A[1:]):
    m = min(m,abs(a-na))

print(m)
for i in range(m):
    ans = []
    for j in range(n+1):
        ans.append((A[j]+i)//m)
    print(*ans)

