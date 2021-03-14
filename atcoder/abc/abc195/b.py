a,b,w = map(int,input().split())
w *= 1000

mi = 10**10
ma = 0
for i in range(10**6+1):
    if a*i <= w <= b*i:
        ma = max(ma,i)
        mi = min(mi,i)
if ma == 0:
    print("UNSATISFIABLE")
else:
    print(mi,ma)
