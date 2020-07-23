n = int(input())
a = [list(map(int,input().split())) for i in range(n)]

def c(x,y):
    if y < x:
        x,y = y,x
    return x*n+y

e = [[] for i in range(n**2)]
count = [0]*(n**2)
for i in range(n):
    for j in range(n-2):
        y = c(i,a[i][j]-1)
        z = c(i,a[i][j+1]-1)
        count[z] += 1
        e[y].append(z)

q = []

for i in range(n-1):
    for j in range(i+1,n):
        x = c(i,j)
        if count[x] == 0:
            q.append(x)
ans = 0

while q:
    
    ans += 1
    old = q
    q = []
    for nowq in old:
        for nex in e[nowq]:
            count[nex] -= 1
            
            if count[nex] == 0:
                q.append(nex)
if sum(count) > 0:
    print(-1)
else:    
    print(ans)



