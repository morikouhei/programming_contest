h,w,n = map(int,input().split())
L = []
s = set()
for i in range(n):
    r,c,a = map(int,input().split())
    s.add(a)
    L.append((a,r,c,i))
dic = {x:i for i,x in enumerate(sorted(s))}
E = [[] for i in range(len(s))]
for a,r,c,i in L:
    E[dic[a]].append((r,c,i))
ans = [0]*n
dich = {}
dicw = {}
for e in E[::-1]:
    for r,c,i in e:
        cand = 0
        if r in dich:
            cand = max(cand,dich[r]+1)
        
        if c in dicw:
            cand = max(cand,dicw[c]+1)
        ans[i] = cand
    for r,c,i in e:
        dich[r] = max(dich.get(r,0),ans[i])
        dicw[c] = max(dicw.get(c,0),ans[i])
for i in ans:
    print(i)
    