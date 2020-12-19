n,m,t = map(int,input().split())
now = 0
v = n
for i in range(m):
    a,b = map(int,input().split())
    v -= a-now
    if v <= 0:
        break
    v += b-a
    v = min(n,v)
    now = b
v -= t-now
if v <= 0:
    print("No")
else:
    print("Yes")
