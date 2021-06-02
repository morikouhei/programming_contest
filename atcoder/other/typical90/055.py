n,p,q = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(n):
    a = A[i]
    for j in range(i):
        b = a*A[j]%p
        for k in range(j):
            c = b*A[k]%p
            for t in range(k):
                d = c*A[t]%p
                for x in range(t):
                    if d*A[x]%p == q:
                        ans += 1
print(ans)
