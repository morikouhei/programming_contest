import bisect
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
s = set(A+B)
for b in B:
    s.add(b+1)
A.sort()
B.sort()

for x in sorted(s):
    la = bisect.bisect_right(A,x)
    l = bisect.bisect_left(B,x)
    if la >= m-l:
        print(x)
        exit()
