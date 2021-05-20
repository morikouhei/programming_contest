from collections import deque
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def solve():
    n,s = map(int,input().split())
    e = [[] for i in range(n)]
    for i in range(n-1):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        e[u].append((v,w))
        e[v].append((u,w))

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
        for nex,_ in e[now]:
            if dep[nex] < dep[now]:
                continue
            lea = 0
            par[nex] = now
            dep[nex] = dep[now]+1
            q.append(nex)
        if lea:
            count[now] = 1
    cum = 0
    h = []
    for now in topo[::-1]:
        c = count[now]
        for nex,w in e[now]:
            if dep[nex] > dep[now]:
                continue
            heappush(h, ((-w+(w//2))*c,w))
            cum += c*w
            count[nex] += c
    ans = 0
    while cum > s:
        a,w = heappop(h)
        a *= -1
        nw = w//2
        c = a//(w-nw)
        ans += 1
        cum -= a

        heappush(h, ((-nw+(nw//2))*c,nw))
    return ans


t = int(input())
for _ in range(t):

    print(solve())