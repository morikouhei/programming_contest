x,a,d,n = map(int,input().split())

if d == 0:
    print(abs(x-a))
    exit()

l = a
r = a + (n-1)*d

if l > r:
    l,r = r,l

if x <= l:
    print(l-x)
elif x >= r:
    print(x-r)
else:
    s = a%(abs(d))
    xx = x%abs(d)
    ans = min(abs(s-xx),abs(d)-abs(s-xx))

    print(ans)