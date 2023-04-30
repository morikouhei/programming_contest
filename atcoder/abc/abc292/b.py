n,q = map(int,input().split())
dic = {}
for i in range(q):
    t,x = map(int,input().split())
    if t <= 2:
        dic[x] = dic.get(x,0)+t
    else:
        f = dic.get(x,0)
        if f >= 2:
            print("Yes")
        else:
            print("No")