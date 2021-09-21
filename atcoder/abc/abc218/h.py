n,R = map(int,input().split())
A = list(map(int,input().split()))
B = [0]*n
for i in range(n-1):
    B[i] += A[i]
    B[i+1] += A[i]
R = min(R,n-R)
inf = 10**10
def search(x):
    dp = [-inf,0]
    ep = [0,0]
    for i in range(n):
        ndp = [ep[0]+B[i]-x,ep[1]+1]
        nep = max(dp,ep)
        dp = ndp
        ep = nep
    return max(dp,ep)

l = 0
r = 1<<31
while r > l + 1:
    m = (r+l)//2
    x,y = search(m)
    if y >= R:
        l = m
    else:
        r = m
x,y = search(l)
print(x+R*l)
