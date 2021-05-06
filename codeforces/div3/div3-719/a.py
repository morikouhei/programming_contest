t = int(input())
for _ in range(t):
    n = int(input())
    S = input()
    count = [0]*26
    ok = 0
    bef = -1
    for s in S:
        ind = ord(s)-ord("A")
        if count[ind] and bef != ind:
            ok = 1
        count[ind] += 1
        bef = ind
    if ok:
        print("NO")
    else:
        print("YES")