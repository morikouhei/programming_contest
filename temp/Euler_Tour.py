def Euler_Tour(x):
    
    par = [-1]*n
    dis = [n]*n
    dis[x] = 0
    stack = [~x,x]
    ET = []
    count = 0
    while stack:
        now = stack.pop()
        count += 1
        if now >= 0:
            ET.append(now)
            for nex in e[now]:
                if par[x] == nex or dis[nex] < dis[now]:
                    continue
                par[nex] = x
                dis[nex] = dis[now]+1
                stack.append(~nex)
                stack.append(nex)

        else:
            ET.append(-1*now-1)

    return ET