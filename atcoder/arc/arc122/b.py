n = int(input())
A = list(map(int,input().split()))

l = 0
r = max(A)+1
s = sum(A)
def calc(x):
    count = 0
    for a in A:
        count -= min(a,2*x)
    return x*n+s+count
eps = 10**(-7)
while r > l+eps:
    c1 = (r+l*2)/3
    c2 = (2*r+l)/3
    if calc(c1) > calc(c2):
        l = c1
    else:
        r = c2
print(calc(l)/n)
