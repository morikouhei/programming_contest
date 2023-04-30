n = int(input())
RCX = [list(map(int,input().split())) for i in range(n)]

R = {}
C = {}

s = set()
for r,c,x in RCX:
    R[r] = R.get(r,0)+x
    C[c] = C.get(c,0)+x
    s.add((r<<30)+c)


sR = [[v,k] for k,v in R.items()]
sR.sort(reverse=True)

sC = [[v,k] for k,v in C.items()]
sC.sort(reverse=True)

ans = 0
for v,r in sR:

    for nv,c in sC:
        if (r<<30)+c in s:
            continue
        ans = max(ans,v+nv)
        break

for r,c,x in RCX:

    v = R[r]+C[c]-x
    ans = max(ans,v)
print(ans)