n = int(input())
at = [tuple(map(int,input().split())) for i in range(n)]
q = int(input())
x = list(map(int,input().split()))

l = -10**20
r = 10**20
base = 0
for a,t in at:
    if t == 1:
        l += a
        r += a
        base += a
    elif t == 2:
        l = max(l,a)
        r = max(r,a)
    else:
        l = min(l,a)
        r = min(r,a)

for i in x:
    print(min(r,max(l,i+base)))