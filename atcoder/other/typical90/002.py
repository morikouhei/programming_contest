n = int(input())

for cand in range(2**n):

    dif = 0
    lis = []
    for i in range(n)[::-1]:
        if cand >> i & 1:
            dif -= 1
            lis.append(")")
        else:
            dif += 1
            lis.append("(")
        if dif < 0:
            break
    if dif != 0:
        continue
    print(*lis, sep="")