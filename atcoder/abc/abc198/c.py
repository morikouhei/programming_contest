R,x,y = map(int,input().split())

if R**2 > x**2+y**2:
    print(2)
    exit()

l = -1
r = 10**20
while r > l+1:
    m = (r+l)//2
    if (R*m)**2 >= x**2+y**2:
        r = m
    else:
        l = m
print(r)