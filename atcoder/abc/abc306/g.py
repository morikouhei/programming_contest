import sys
sys.setrecursionlimit(3*10**5)
input = sys.stdin.readline
import math

def solve():
    n,m = map(int,input().split())
    e = [[] for i in range(n)]
    re = [[] for i in range(n)]
    for _ in range(m):
        u,v = [int(x)-1 for x in input().split()]
        e[u].append(v)
        re[v].append(u)

    vis = [0]*n
    vis[0] = 1
    q = [0]
    while q:
        now = q.pop()
        for nex in re[now]:
            if vis[nex]:
                continue
            q.append(nex)
            vis[nex] = 1


    
    dist = [-1]*n
    q = [[0,-1,0]]
    while q:

        now,p,d = q.pop()
        if dist[now] != -1:
            continue
        dist[now] = d

        for nex in e[now]:
            if vis[nex] == 0 or nex == p or dist[nex] != -1: 
                continue
            
            q.append([nex,now,d+1])

    g = 0
    for i in range(n):
        if vis[i] == 0 or dist[i] == -1:
            continue
        
        for nex in e[i]:
            if dist[nex] != -1:
                g = math.gcd(g,abs(dist[i]+1-dist[nex]))

    
    if g == 0:
        return "No"

    while g % 2 == 0:
        g //= 2

    while g % 5 == 0:
        g //= 5

    if g == 1:
        return "Yes"
    else:
        return "No"



t = int(input())
for _ in range(t):
    print(solve())