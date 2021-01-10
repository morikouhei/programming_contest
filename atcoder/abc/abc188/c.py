n = int(input())
a = list(map(int,input().split()))
now = [i for i in range(len(a))]
for i in range(n-1):
    nex = []
    for j in range(0,len(now),2):
        x,y = a[now[j]],a[now[j+1]]
        if x >= y:
            nex.append(now[j])
        else:
            nex.append(now[j+1])
    now = nex
x,y = a[now[0]],a[now[1]]
if x >= y:
    print(now[1]+1)
else:
    print(now[0]+1)
