import bisect
n = int(input())

lis = [[] for i in range(n+5)]

A = list(map(int,input().split()))
for i,a in enumerate(A):
    lis[a].append(i)

q = int(input())
for _ in range(q):
    l,r,x = map(int,input().split())

    if lis[x] == []:
        print(0)
        continue
    l -= 1
    lind = bisect.bisect_left(lis[x],l)
    rind = bisect.bisect_left(lis[x],r)
    print(rind-lind)