import bisect
n = int(input())
A = list(map(int,input().split()))
sA = A[:]
sA.sort()
cum = [0]
for a in sA:
    cum.append(a+cum[-1])

for a in A:
    pos = bisect.bisect_right(sA,a)
    print(cum[-1]-cum[pos])