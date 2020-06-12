import sys
sys.setrecursionlimit(10**7)

n = int(input())
d = []
c0 = c1 = 0
for i in range(n):
    a,b,c = map(int,input().split())
    d.append([a,b,c])
    if b:
        c0 += 1
    if c:
        c1 += 1

e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)
if c0 != c1:
    print(-1)
    exit()

 
count = [[0] for i in range(n)]

def dfs1(x,p):
    c1 = 0
    c2 = 0
    if d[x][1] == 0 and d[x][2] == 1:
        c1 += 1
    elif d[x][1] != d[x][2]:
        c2 += 1
    for nex in e[x]:
        if nex == p:
            continue
        a,b = dfs1(nex,x)
        c1 += a
        c2 += b
    count[x] = [c1,c2]
    return c1,c2

dfs1(0,-1)
print(count)
