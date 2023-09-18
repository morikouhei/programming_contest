loop = {}
used = {}

def period(S,x):

    num = len(S)//x

    for i in range(x):

        base = S[i]

        for j in range(num):
            if base != S[j*x+i]:
                return 0
    
    return 1

ans = []
n = int(input())
for _ in range(n):
    S = input()
    le = len(S)

    for i in range(1,le+1):
        if le%i:
            continue
        if period(S,i):
            cycle = S[:i]
            break
    

    if cycle not in used:
        used[cycle] = set()

    bind = le//len(cycle)
    sid = loop.get((cycle,bind),bind)

    while sid in used[cycle]:
        sid += bind
    ans.append(sid//bind)
    used[cycle].add(sid)
    loop[(cycle,bind)] = sid+bind

print(*ans)
