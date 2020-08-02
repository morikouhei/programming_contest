import sys 
sys.setrecursionlimit(320000)
input = sys.stdin.readline
def dfs(x,pa):
    g = 0
    b = 0
    for nex in e[x]:
        if nex == pa:
            continue
        ng,nb,check = dfs(nex,x)
        if check == False:
            return 0,0,False
        g += ng
        b += nb
    
    c = p[x]
    num = h[x]
    if num%2 != (c%2+(g-b)%2)%2:        
        return 0,0,False
    if num > g+b+c or num < g-b-c:
        return 0,0,False
    now = g-b
    if num >= now:
        g += num-now
        g += (c-num+now)//2
        b += (c-num+now)//2
    else:
        b += now-num
        g += (c+num-now)//2
        b += (c+num-now)//2
    
    return g,b,True

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    h = list(map(int,input().split()))
    e = [[] for i in range(n)]
    for i in range(n-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        e[a].append(b)
        e[b].append(a)
    g,b,check = dfs(0,-1)
    if check:
        print("YES")
    else:
        print("NO")