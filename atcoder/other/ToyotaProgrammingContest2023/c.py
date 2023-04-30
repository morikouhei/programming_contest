l,r = map(int,input().split())
ans = 0
M = r-l+1

for i in range(1,M):
    dic = {}

    li = l//i
    ri = (r+i-1)//i
    for j in range(li,ri+1):
        x = j*i
        if x < l:
            continue
        if x > r:
            break
        
        y = x^i
        ans += dic.get(y,0)
        dic[x] = dic.get(x,0)+1
print(ans)