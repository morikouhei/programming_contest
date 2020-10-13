import itertools

n,m = map(int,input().split())
w = list(map(int,input().split()))
M = 10**8+1
vm = 10**9
V = [0]*M
for i in range(m):
    l,v = map(int,input().split())
    vm = min(v,vm)
    V[v] = max(l,V[v])

if vm < max(w):
    print(-1)
    exit()

for i in range(1,M):
    V[i] = max(V[i],V[i-1])
ans = 10**9

for x in itertools.permutations(w):
    l = []
    for i in range(n):
        now = x[i]
        dis = 0
        for j in range(i-1,-1,-1):
            now += x[j]
            if now > M:
                dis = max(dis,V[-1]+l[j])
                break
            dis = max(dis,V[now-1]+l[j])
            
        l.append(dis)  
        if dis >= ans:
            break
    ans = min(ans,dis)

print(ans)
