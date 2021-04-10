import math
def solve():

    a,q = map(int,input().split())
    L = []
    p = []
    for i in range(a):
        s,t = input().split()
        t = int(t)
        L.append(s)
        p.append(t)
    ans = [0,0]
    anss = ""
    for i in range(q):
        t = 1
        b = q**q
        for j in range(a):
            if L[j][i] == "T":
                t *= p[j]
            else:
                t *= q-p[j]
            
        f = 1
        for j in range(a):
            if L[j][i] == "F":
                f *= p[j]
            else:
                f *= q-p[j]
        if t >= f:
            anss += "T"
            gcd = math.gcd(t, t+f)
            c = t//gcd
            b = (t+f)//gcd
            
        else:
            anss += "F"
            gcd = math.gcd(f, t+f)
            c = f//gcd
            b = (t+f)//gcd
        
        if ans == [0,0]:
            ans = [c,b]
        else:
            x,y = ans
            c1 = x*b
            c2 = y*c
            b = b*y
            c = c1+c2
            gcd = math.gcd(b, c)
            c //= gcd
            b //= gcd
            ans = [c,b]
    return anss, ans

T = int(input())
for t in range(T):
    anss,ans = solve()
    print("Case #{}: {} {}/{}".format(t+1,anss,ans[0],ans[1]))