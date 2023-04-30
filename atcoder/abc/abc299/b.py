n,t = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))

mT = [-1,-1]
m0 = [0,R[0]]
c0 = C[0]

for i,(c,r) in enumerate(zip(C,R)):
    if c == t:
        if mT[0] < r:
            mT = [r,i+1]
    elif c == c0:
        if m0[0] < r:
            m0 = [r,i+1]

if mT != [-1,-1]:
    print(mT[1])
else:
    print(m0[1])