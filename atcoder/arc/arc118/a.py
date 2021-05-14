t,n = map(int,input().split())

l = 0
r = 10**15
while r > l + 1:
    m = (r+l)//2
    if t*m//100 >= n:
        r = m
    else:
        l = m

print((100+t)*l//100+1)