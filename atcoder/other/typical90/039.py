import sys
sys.setrecursionlimit(2*10**5)
n = int(input())
e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

dis = [0]*n
count = [0]*n
def dfs(x,p=-1):
    d = 0
    num = 1
    for nex in e[x]:
        if nex == p:
            continue
        nd,nnum = dfs(nex,x)
        d += nd+nnum
        num += nnum
    dis[x] = d
    count[x] = num
    return d,num

dfs(0)
ans = 0
def dfs2(x,p,cum,chi):
    global ans
    
    cum += dis[x]+chi
    ans += cum

    for nex in e[x]:
        if nex == p:
            continue

        dfs2(nex,x,cum-dis[nex]-count[nex],n-count[nex])

dfs2(0,-1,0,0)
print(ans//2)