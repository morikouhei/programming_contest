n,a,b = map(int,input().split())
A = list(map(int,input().split()))
A.sort()


def solve(x):
    count = 0
    for i in A:
        if i >= x:
            count += (i-x)//b
        else:
            count -= (x-i+a-1)//a
    
    return count >= 0
l = 1
r = 10**9+5

while r > l + 1:
    m = (r+l)//2
    if solve(m):
        l = m
    else:
        r = m
print(l)

