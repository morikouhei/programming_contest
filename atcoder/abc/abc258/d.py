n,x = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
ans = 10**20
mi = 10**20
count = 0
s = 0
for a,b in AB:
    s += 1
    count += a+b
    mi = min(mi,b)
    num = count + max(0,x-s)*mi
    print(x,s,mi,num)
    ans = min(ans,count)
print(ans)