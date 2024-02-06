def is_ok(x,y):

    dif = y.count("A") - x.count("A")
    dif2 = y.count("A") - x.count("A")
    if dif < 0 or dif2 < 0:
        return 0
    anum = 0
    for i in range(len(x)):
        if x[i] == "C":
            if dif > 0:
                x[i] = "A"
            else:
                x[i] = "B"
        
            dif -= 1

        if x[i] == "A":
            anum += 1
        if y[i] == "A":
            anum -= 1
        
        if anum < 0:
            return 0
    return 1
    

def solve():
    n,x,y = input().split()
    n = int(n)

    ok = 1
    lx = []
    ly = []
    for nx,ny in zip(x,y):
        if ny == "C":
            if nx != "C":
                return "No"
            else:
                ok &= is_ok(lx,ly)
            lx = []
            ly = []
        else:
            lx.append(nx)
            ly.append(ny)

    ok &= is_ok(lx,ly)

    return "Yes" if ok else "No"

t = int(input())
for _ in range(t):
    print(solve())