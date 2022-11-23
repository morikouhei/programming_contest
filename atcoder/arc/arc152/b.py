from bisect import bisect_left
n,l = map(int,input().split())
A = list(map(int,input().split()))
inf = 10**20
A = A + [2*l-a for a in A] + [inf]
ans = inf
for i in range(n):
    a = A[i]
    nind = bisect_left(A,a+l)
    dl = A[nind-1]
    ans = min(ans,2 * (2*l - (dl-a)))
    dr = A[nind]
    ans = min(ans,2*(dr-a))
print(ans)