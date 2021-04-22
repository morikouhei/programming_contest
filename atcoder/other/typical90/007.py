import bisect

n = int(input())
inf = 10**20
A = list(map(int,input().split()))+[-inf,inf]
A.sort()

q = int(input())
for i in range(q):
    b = int(input())
    ind = bisect.bisect_left(A, b)
    print(min(b-A[ind-1],A[ind]-b))