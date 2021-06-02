import sys

fib = [1,2]
for i in range(20):
    fib.append(fib[-1]+fib[-2])

def solve():
    n = int(input())
    num = [-1]*1600
    for i in range(n+1,1600):
        num[i] = -100
    ans = 0
    def ask(x):
        if num[x] == -1:
            print("?",x)
            sys.stdout.flush()
            num[x] = int(input())
        return num[x]
    if n <= 5:
        for i in range(n):
            ans = max(ans,ask(i+1))
    else:
        cl = 0
        cr = 1597
        dl = 610
        dr = 987
        el = ask(dl)
        er = ask(dr)
        ans = max(ans,el,er)
        if el < er:
            cl = dl
            dl = dr
            dr = -1
            el = er
            er = -1
        else:
            cr = dr
            dr = dl
            dl = -1
            er = el
            el = -1

        for i in range(12,-1,-1):
            if dl == -1:
                dl = cl+fib[i]
                el = ask(dl)
            elif dr == -1:
                dr = cr-fib[i]
                er = ask(dr)
            ans = max(ans,el,er)
            if el < er:
                cl = dl
                dl = dr
                dr = -1
                el = er
                er = -1
            else:
                cr = dr
                dr = dl
                dl = -1
                er = el
                el = -1

        for i in range(cl+1,cr):
            ans = max(ans,ask(i))
    
    print("!",ans)
    sys.stdout.flush()

t = int(input())
for _ in range(t):
    solve()