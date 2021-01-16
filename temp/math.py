def floor_sum(n,m,a,b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2;
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = (y_max * m - b)
    if y_max == 0:
        return ans
    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans

### get the value of 10**x == b (mod mod)
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