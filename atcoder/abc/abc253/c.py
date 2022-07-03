from heapq import heappush,heappop

dic = {}
q = int(input())
maxh = []
minh = []

for _ in range(q):
    l = list(map(int,input().split()))
    if l[0] == 1:
        x = l[1]
        dic[x] = dic.get(x,0)+1
        heappush(minh,x)
        heappush(maxh,-x)
    elif l[0] == 2:
        _,x,c = l
        
        if x in dic:
            dic[x] -= min(dic[x],c)
    
    else:
        ma = 0
        mi = 10**10
        while maxh:
            cand = -maxh[0]
            if dic.get(cand,0) == 0:
                heappop(maxh)

            else:
                ma = cand
                break

        while minh:
            cand = minh[0]
            if dic.get(cand,0) == 0:
                heappop(minh)

            else:
                mi = cand
                break

        print(ma-mi)