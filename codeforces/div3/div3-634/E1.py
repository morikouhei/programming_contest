t = int(input())

for q in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    sl = [[] for i in range(201)]
    ss = [[0] for i in range(201)]
    for i in range(n):
        sl[l[i]].append(i)
        for j in range(201):
            ss[j].append(ss[j][-1])
        ss[l[i]][-1] += 1

    ans = 0
    for i in range(200):
        if not sl[i]:
            continue
        if len(sl[i]) == 1:
            ans = max(ans,1)
            continue
        for j in range(len(sl[i])//2):
            le = sl[i][j]
            ri = sl[i][-1-j]
            for k in range(200):
                if i == k:
                    ans = max(ans,len(sl[i]))
                    continue
                if sl[k]:
                    ans = max(ans,2*(j+1)+ss[k][ri]-ss[k][le])

                
    print(ans)
