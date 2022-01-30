n,x = map(int,input().split())
L = [list(map(int,input().split())) for i in range(n)]
dic = {}
dic[x] = 1
for i in range(n):
    ndic = {}
    for a in L[i][1:]:
        if x%a:
            continue
        for k,v in dic.items():
            if k%a:
                continue
            ndic[k//a] = ndic.get(k//a,0)+v
    dic = ndic
print(dic.get(1,0))
