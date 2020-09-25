
def extgcd(a,b):
    if b == 0:
        return a,1,0
    else:
        g,y,x = extgcd(b,a%b)
        y -= a//b*x
        return g,x,y

def crt(b1,m1,b2,m2):
    if m2 > m1:
        m1,m2 = m2,m1
        b1,b2 = b2,b1
    g,x,y = extgcd(m1,m2)
    if g != 1:
        return float("INF")
    m = m1*m2
    ans = (b1+m1*(b2-b1)*x%m2)%m 
    if ans == 0:
        ans = m
    return ans

n = int(input())*2
ans = n

for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        ans = min(ans,crt(0,i,-1,n//i))       
        ans = min(ans,crt(0,n//i,-1,i))
print(ans)