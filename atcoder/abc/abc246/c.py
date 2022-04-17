n,k,x = map(int,input().split())
A = list(map(int,input().split()))

for i,a in enumerate(A):
    c = a//x
    dk = min(k,c)
    k -= dk
    A[i] -= x*dk

A.sort()
ans = 0
for a in A[::-1]:
    if k:
        k -= 1
    else:
        ans += a
print(ans)