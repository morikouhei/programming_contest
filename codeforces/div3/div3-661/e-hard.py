from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.buffer.readline
 
def solve():
    n,s = map(int,input().split())
    e = [[] for i in range(n)]
    for i in range(n-1):
        u,v,w,c = map(int,input().split())
        u -= 1
        v -= 1
        e[u].append((v,w,c))
        e[v].append((u,w,c))
 
    par = [-1]*n
    dep = [n]*n
    dep[0] = 0
    topo = []
    q = deque([0])
    count = [0]*n
    while q:
        now= q.pop()
        topo.append(now)
        lea = 1
        for nex,_,_ in e[now]:
            if dep[nex] < dep[now]:
                continue
            lea = 0
            par[nex] = now
            dep[nex] = dep[now]+1
            q.append(nex)
        if lea:
            count[now] = 1
    cum = 0
    h1 = [0]
    h2 = []
    for now in topo[::-1]:
        num = count[now]
        for nex,w,c in e[now]:
            if dep[nex] > dep[now]:
                continue
            cum += num*w
            count[nex] += num
            if c == 2:
                while w:
                    h2.append((w-w//2)*num)
                    w //= 2
            else:
                while w:
                    h1.append((w-w//2)*num)
                    w //= 2
    if cum <= s:
        return 0
    h1.sort(reverse=True)
    h2.sort(reverse=True)
    h2cum = [0]*(len(h2)+1)
    for i in range(len(h2)):
        h2cum[-2-i] = h2cum[-1-i]+h2[i]
 
    ans = 10**10
    now = 0
    le = len(h2cum)
    for i in range(len(h1)):
        h = h1[i]
        if cum-h2cum[0] > s:
            cum -= h
            continue
        while now < le and cum-h2cum[now] <= s:
            now += 1
        if ans > i+(le-now)*2:
            ans = i+(le-now)*2
        cum -= h 
    return ans
 
 
t = int(input())
for _ in range(t):
 
    print(solve())