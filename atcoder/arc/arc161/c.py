def solve():
    n = int(input())

    e = [[] for i in range(n)]

    for _ in range(n-1):
        a,b = [int(x)-1 for x in input().split()]
        e[a].append(b)
        e[b].append(a)

    S = input()

    topo = []
    vis = [0]*n
    q = [0]

    vis[0] = 1
    par = [-1]*n
    while q:
        now = q.pop()
        topo.append(now)

        for nex in e[now]:
            if vis[nex]:
                continue
            vis[nex] = 1
            par[nex] = now
            q.append(nex)


    

    col = [""]*n

    for now in topo[1:][::-1]:

        p = par[now]

        if p != -1 and col[now] == "":
            ps = S[p]
            col[now] = ps

        nw = 0
        nb = 0
        both = 0
        for nex in e[now]:
            if nex == p:
                continue

            if col[nex] == "B":
                nb += 1
            elif col[nex] == "W":
                nw += 1
            else:
                both += 1

        
        s = S[now]
        if s == "B":
            nb += both
        else:
            nw += both

        if s == "B":
            if nb > nw+1:
                pass

            elif nb == nw:
                pc = col[p]
                if pc == "W":
                    return -1
                col[p] = "B"
            else:
                return -1

            
        elif s == "W":
            if nw > nb+1:
                pass

            elif nb == nw:
                pc = col[p]
                if pc == "B":
                    return -1
                col[p] = "W"
            else:
                return -1
        
    
    nb = 0
    nw = 0
    for nex in e[0]:
        if col[nex] == "B":
            nb += 1
        else:
            nw += 1
    
    if S[0] == "B":
        if nb < nw:
            return -1

    else:
        if nw < nb:
            return -1
        
    for i in range(n):
        if col[i] == "":
            col[i] = "W"
    
    return "".join(col)

t = int(input())
for _ in range(t):
    print(solve())



        


        
