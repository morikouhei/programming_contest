t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for a,na in zip(A,A[1:]):
        mi,ma = min(a,na),max(a,na)
        while ma/mi > 2:
            ans += 1
            mi *= 2
    print(ans)