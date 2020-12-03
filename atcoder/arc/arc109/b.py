n = int(input())
l = 0
r = n+5
while r > l + 1:
    m = (r+l)//2
    d = m*(m+1)//2
    if d <= n+1:
        l = m
    else:
        r = m
print(n-l+1)