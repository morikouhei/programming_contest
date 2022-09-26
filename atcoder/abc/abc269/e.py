import sys

n = int(input())

l = 0
r = n

while r > l + 1:
    m = (r+l)//2

    print("?",1,n,1,m)
    sys.stdout.flush()
    t = int(input())

    if t == m:
        l = m
    else:
        r = m

x = r

l = 0
r = n

while r > l + 1:
    m = (r+l)//2

    print("?",1,m,1,n)
    sys.stdout.flush()
    t = int(input())

    if t == m:
        l = m
    else:
        r = m

y = r

print("!",y,x)
sys.stdout.flush()