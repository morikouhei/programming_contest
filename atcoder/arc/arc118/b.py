k,n,m = map(int,input().split())
A = list(map(int,input().split()))

def calc(x):
    mi = 0
    ma = 0
    for a in A:
        ma += (x+a*m)//n
        mi += (-x+a*m+n-1)//n
        if mi > ma:
            return False
    return mi <= m <= ma

l = -1
r = n*m+1
while r > l + 1:
    c = (r+l)//2
    if calc(c):
        r = c
    else:
        l = c

L = []
R = []
for a in A:
    R.append((r+a*m)//n)
    L.append(max(0,(-r+a*m+n-1)//n))
ans = R.copy()
s = sum(ans)

for i in range(k):
    if s > m:
        dif = R[i]-L[i]
        if dif <= s-m:
            ans[i] = L[i]
            s -= dif
        else:
            ans[i] -= s-m
            s = m

print(*ans)