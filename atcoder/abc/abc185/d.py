n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a = [0]+a+[n+1]

dif = n
l = []
for i in range(1,m+2):
    x = a[i]-a[i-1]-1
    if x == 0:
        continue
    dif = min(dif,x)
    l.append(x)
if l == []:
    print(0)
    exit()
ans = 0
for i in l:
    ans += (i+dif-1)//dif
print(ans) 
    
