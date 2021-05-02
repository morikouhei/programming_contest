def check(x,y):
    L = set()
    L.add(x)
    if x == y:
        return 0 
    for i in range(20):
        nL = set()
        for j in L:
            nL.add(j*2)
            now = 0
            if j == 0:
                nL.add(1)
            for k in range(j.bit_length()):
                if j >> k & 1:
                    continue
                now += 1<<k
            nL.add(now)
        L = nL
        if y in L:
            return i+1
    return "IMPOSSIBLE"
def solve():
    s,e = input().split()
    s = s[::-1]
    ss = 0
    ee = 0
    e = e[::-1]
    for i in range(len(s)):
        if s[i] == "1":
            ss += 1<<i
    for i in range(len(e)):
        if e[i] == "1":
            ee += 1<<i
    return check(ss,ee)
        
T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1,ans))