n = int(input())
ST = [input().split() for i in range(n)]
for i in range(n):
    s,t = ST[i]
    ok = [1,1]
    for j in range(n):
        if i == j:
            continue
        ns,nt = ST[j]
        if s == ns or s == nt:
            ok[0] = 0
        if t == ns or t == nt:
            ok[1] = 0
    if sum(ok) == 0:
        print("No")
        exit()
print("Yes")