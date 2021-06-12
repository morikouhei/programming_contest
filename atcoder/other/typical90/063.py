h,w = map(int,input().split())
P = [list(map(int,input().split())) for i in range(h)]

ans = 0
for i in range(1,1<<h):
    l = []
    for j in range(h):
        if i >> j & 1:
            l.append(j)
    dic = {}
    for j in range(w):
        last = -1
        for k in l:
            if last == -1:
                last = P[k][j]
            else:
                if last != P[k][j]:
                    last = -2
                    break
        dic[last] = dic.get(last,0)+1
    for i,j in dic.items():
        if i == -2:
            continue
        ans = max(ans,j*len(l))
print(ans)
    
