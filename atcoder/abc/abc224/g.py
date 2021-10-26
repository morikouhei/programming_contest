n,s,t,a,b = map(int,input().split())

def search(x):
    if x <= s <= t:
        return (t-s)*a

    return n/(t-x+1)*b+(t-x)/2*a
ans = n*b
l = 1
r = t
while r > l+2:
    c1 = (2*l+r)//3
    c2 = (l+2*r)//3
    if search(c1) >= search(c2):
        l = c1
    else:
        r = c2

for i in range(l,r+1):
    ans = min(ans,search(i))
print(ans)

