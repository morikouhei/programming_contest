def Lowlink(graph):
    n = len(graph)
    order = [-1]*n
    low = [n]*n
    par = [-1]*n
    vis = 0
    for root in range(n):
        if order[root] != -1:
            continue
        q = [root]
        while q:
            now = q.pop()

            if now < 0:
                now = ~now
                if now == root:
                    continue
                p = par[now]
                low[p] = min(low[p],low[now])
                continue

            if order[now] >= 0:
                continue
            order[now] = vis
            low[now] = vis
            vis += 1
            q.append(~now)

            check = 0
            for nex in graph[now]:
                if par[now] == nex and check == 0:
                    check += 1
                    continue
                elif order[nex] >= 0:
                    if low[now] < 0 or order[nex] < low[now]:
                        low[now] = order[nex]
                else:
                    par[nex] = now
                    q.append(nex)

    briges = []
    for i in range(n):
        if par[i] < 0:
            continue
        if low[i] < 0 or low[i] > order[par[i]]:
            briges.append((i,par[i]))

    return briges