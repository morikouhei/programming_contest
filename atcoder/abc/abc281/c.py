n,t = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
m = t%s
for i,a in enumerate(A,1):
    if a <= m:
        m -= a
        continue
    print(i,m)
    exit()