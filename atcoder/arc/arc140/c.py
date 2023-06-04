import bisect
n,x = map(int,input().split())


def score(A):
    lis = []
    for a,na in zip(A,A[1:]):
        da = abs(a-na)
        if lis == []:
            lis.append(da)
            continue

        bind = bisect.bisect_left(lis,da)
        if bind < len(lis):
            lis[bind] = da
        else:
            lis.append(da)

    return len(lis)


def make(ind,pos):

    A = [x,ind]
    l = ind-1
    r = ind+1

    while True:

        if pos:
            if r == x:
                r += 1
            if r <= n:
                A.append(r)

            if l == x:
                l -= 1
            if l >= 1:
                A.append(l)

            r += 1
            l -= 1

            if l < 1 and r > n:
                break
        else:
            if l == x:
                l -= 1
            if l >= 1:
                A.append(l)

            if r == x:
                r += 1
            if r <= n:
                A.append(r)

            r += 1
            l -= 1

            if l < 1 and r > n:
                break

    return A


ans = 0
cand = []

for s in range(n//2-1,n//2+2):
    if s == x or s == 0:
        continue
    ncand = make(s,1)
    nans = score(ncand)
    if nans > ans:
        ans = nans
        cand = ncand
    
    ncand = make(s,0)
    nans = score(ncand)

    if nans > ans:
        ans = nans
        cand = ncand

print(*cand)
