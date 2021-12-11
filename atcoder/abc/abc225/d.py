n,q = map(int,input().split())
top = [-1]*(n+1)
bottom = [-1]*(n+1)
for i in range(q):
    l = list(map(int,input().split()))
    if l[0] == 3:
        now = l[1]
        while top[now] != -1:
            now = top[now]
        ans = []
        while now != -1:
            ans.append(now)
            now = bottom[now]
        print(len(ans),*ans)
        continue
    t,x,y = l
    if t == 1:
        bottom[x] = y
        top[y] = x
    else:
        bottom[x] = -1
        top[y] = -1