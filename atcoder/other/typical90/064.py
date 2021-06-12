n,q = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
dif = []
for a,na in zip(A,A[1:]):
    ans += abs(a-na)
    dif.append(a-na)

for _ in range(q):
    l,r,v = map(int,input().split())
    l -= 1
    r -= 1
    if l != 0:
        ans -= abs(dif[l-1])
        dif[l-1] -= v
        ans += abs(dif[l-1])
    if r != n-1:
        ans -= abs(dif[r])
        dif[r] += v
        ans += abs(dif[r])
    print(ans)