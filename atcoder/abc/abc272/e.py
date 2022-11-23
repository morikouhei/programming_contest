n,m = map(int,input().split())

A = list(map(int,input().split()))

mex = [set() for i in range(m+1)]

for i,a in enumerate(A,1):
    l = max(0,(-a+i-1)//i)
    r = min((n-a)//i,m)
    if r < l:
        continue
    if l > m:
        continue

    for j in range(l,r+1):
        na = a+i*j
        mex[j].add(na)

for i in range(1,m+1):
    me = mex[i]
    for j in range(n+2):
        if j not in me:
            print(j)
            break

