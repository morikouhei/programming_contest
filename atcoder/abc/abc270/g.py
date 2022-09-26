
def baby_step_giant_step(a,b,mod):
    a %= mod
    b %= mod
    l = int(mod**0.5)+1
    h = 1 if mod != 0 else 0
    dic = {}
    ### if b = 1, add (h == b and i != 0)
    for i in range(l):
        if h == b:
            return i
        dic[h*b%mod] = i
        h *= a
        h %= mod
    g = h
    for i in range(l):
        if g in dic:
            res = (i+1)*l-dic[g]
            if pow(a,res,mod) == b:
                return res
            else:
                return -1
        g *= h
        g %= mod
    return -1

def solve():
    p,a,b,s,g = map(int,input().split())

    if s == g:
        return 0

    if a == 0:
        if b == g:
            return 1
        else:
            return -1

    if a == 1:
        if b == 0:
            return -1
        g = (g-s)%p
        ans = g*pow(b,p-2,p)%p
        return ans
        
    b = b*pow(a-1,p-2,p)%p
    g = (g+b)%p
    s = (s+b)%p

    if s == 0:
        return -1

    ans = baby_step_giant_step(a,g*pow(s,p-2,p)%p,p)
    return ans


t = int(input())
for _ in range(t):
    print(solve())