from collections import defaultdict
n,a = map(int,input().split())
WXV = [list(map(int,input().split())) for i in range(n)]

ans = 0

for i in range(n):
    w,x,v = WXV[i]

    dic = defaultdict(list)
    base = w
    for j in range(n):
        if i == j:
            continue
        nw,nx,nv = WXV[j]

        if v == nv:
            if x <= nx <= x+a:
                base += nw
        
            continue

        if (x + a < nx and v < nv) or (nx < x and v > nv):
            continue

        t1 = (nx-x-a)/(v-nv)
        t2 = (nx-x)/(v-nv)        
        tin,tout = max(min(t1,t2),0),max(t1,t2)

        dic[tin].append(nw)
        dic[tout].append(-nw)
    
    ans = max(ans,base)
    keys = sorted(dic.keys())
    for key in keys:
        dic[key].sort(reverse=True)
        for weight in dic[key]:
            base += weight
            ans = max(ans,base)
print(ans)