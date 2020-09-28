
def extgcd(a,b):
    if b == 0:
        return a,1,0
    g,y,x = extgcd(b,a%b)
    y -= a//b*x
    return g,x,y

def calc(m1):
    m2 = n//m1
    g,x,y = extgcd(m1,m2)
    if g != 1:
        return float("INF")
    x = -x
    while x <= 0:
        x += m2
    return x*m1


n = int(input())*2
ans = n

for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        ans = min(ans,calc(i),calc(n//i))
        
print(ans)