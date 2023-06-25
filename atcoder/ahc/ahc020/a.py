import sys
import time
input = sys.stdin.readline
from heapq import heappop,heappush
import random

class Unionfind:
     
    def __init__(self,n):
        self.uf = [-1]*n
 
    def find(self,x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]
 
    def same(self,x,y):
        return self.find(x) == self.find(y)
 
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.uf[x] > self.uf[y]:
            x,y = y,x
        self.uf[x] += self.uf[y]
        self.uf[y] = x
        return True
 
    def size(self,x):
        x = self.find(x)
        return -self.uf[x]

def isqrt(n):
    root = 0 # Running result.
    rmdr = 0 # Running remainder ``n - root**2``.
    for s in reversed(range(0, n.bit_length(), 2)): # Shift ``n`` by ``s`` bits.
        bits = n >> s & 3 # The next two most significant bits of ``n``.
        rmdr = rmdr << 2 | bits # Increase the remainder.
        cand = root << 2 | 1 # Shifted candidate root value to try.
        bit_next = int(rmdr >= cand) # The next bit in the remainder.
        root = root << 1 | bit_next # Add next bit to running result.
        rmdr -= cand * bit_next # Reduce the remainder if bit was added.
    return root

stime = time.time()
TIME_LIM = 1.7

n,m,k = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(n)]
UVW = []
e = [[] for i in range(n)]
for i in range(m):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    UVW.append([u,v,w])
    e[u].append([v,w,i])
    e[v].append([u,w,i])

AB = [list(map(int,input().split())) for i in range(k)]
P = [0]*n
B = [0]*m

used_house = [0]*k
used_power = [0]*n
used_power[0] = 1
power_pos = [-1]*n

def out():
    print(*P)
    print(*B)
    exit()


def get_dis(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2


def get_p_int(p_square):
    return 1 + isqrt(p_square-1)

def bfs(s):
    dist = [10**10]*n
    dist[s] = 0
    par = [-1]*n

    h = [[0,s]]
    while h:
        d,now = heappop(h)
        if dist[now] != d:
            continue
        for nex,nd,id in e[now]:
            if dist[nex] > d+nd:
                dist[nex] = d+nd
                par[nex] = [now,id]
                heappush(h,[d+nd,nex])


    return dist,par

all_dist = []
all_par = []

for i in range(n):
    dist,par = bfs(i)
    all_dist.append(dist)
    all_par.append(par)

power_to_house_dist = []
# house_to_power_dist = [[] for i in range(k)]
for i,(x,y) in enumerate(XY):
    power_to_house = []
    for j,(a,b) in enumerate(AB):
        d = get_dis(a,b,x,y)
        d = get_p_int(d)
        power_to_house.append([d,j])
        # house_to_power_dist[j].append([d,i])
    power_to_house.sort()
    power_to_house_dist.append(power_to_house)

# for i in range(k):
#     house_to_power_dist[i].sort()



def bsearch_left_power_to_house(id,power):
    l = 0
    r = k+1
    power_to_house = power_to_house_dist[id]
    while r > l + 1:
        m = (r+l)//2
        if power_to_house[m][0] <= power:
            l = m
        else:
            r = m

    return l



dist_list = []
for i,(a,b) in enumerate(AB):
    dis = 10**20
    id = -1
    for j,(x,y) in enumerate(XY):
        d = get_dis(a,b,x,y)
        if dis > d:
            dis = d
            id = j
    
    dist_list.append([-get_p_int(dis),i,id])

dist_list.sort()

for d,house_id,power_id in dist_list:
    if used_house[house_id]:
        continue
    d *= -1
    P[power_id] = d
    used_power[power_id] = 1

    for i,(nd,id) in enumerate(power_to_house_dist[power_id]):
        if nd <= d:
            used_house[id] = 1
        else:
            break
    
edges = []
for i in range(n):
    if used_power[i] == 0:
        continue
    for j in range(i):
        if used_power[j] == 0:
            continue
        edges.append([all_dist[i][j],i,j])

edges.sort()
uf = Unionfind(n)
for _,u,v in edges:
    if uf.same(u,v):
        continue
    uf.union(u,v)
    t = v
    while t != u:
        t,id = all_par[u][t]
        B[id] = 1
    
base_score = 0
for i in range(m):
    if B[i]:
        base_score += UVW[i][2]

for i in range(n):
    base_score += P[i]**2


for i in range(n):
    p = P[i]
    p_target = bsearch_left_power_to_house(i,p)
    power_pos[i] = p_target

times = 0

def clime_update(s,p_nex,base_score,P):
    p_target = bsearch_left_power_to_house(s,p_nex)
    p_nex = power_to_house_dist[s][p_target][0]
    if p_nex <= P[s]:
        return base_score,P

    upds = [[s,p_nex,p_target]]

    cal_del_set = set()

    for d,id in power_to_house_dist[s]:
        if d <= p_nex:
            cal_del_set.add(id)
        else:
            break
    
    for i in range(n):
        if i == s:
            continue

        now_pos = power_pos[i]
        while now_pos >= 0:
            d,id = power_to_house_dist[i][now_pos]
            if id in cal_del_set:
                now_pos -= 1
            else:
                break

        if power_pos[i] > now_pos:
            if now_pos == -1:
                upds.append([i,0,-1])
            else:
                upds.append([i,power_to_house_dist[i][now_pos][0],now_pos])



    dx = 0
    for id,p_nex,pos_nex in upds:
        dx += p_nex ** 2 - P[id] ** 2

    if dx <= 0:
        for id,p_nex,pos_nex in upds:
            P[id] = p_nex
            power_pos[id] = pos_nex
        base_score += dx

    return base_score,P

use_P = []
for i in range(n):
    if P[i]:
        use_P.append(i)

le = len(use_P)

while True:
    
    times += 1
    if times%50 == 0:
        if time.time() - stime > TIME_LIM:
            break
    s = use_P[random.randint(0,le-1)]
    p_max = min(P[s]+1000,5000,power_to_house_dist[s][-1][0])

    p_nex = random.randint(P[s]+1,p_max)

    base_score,P = clime_update(s,p_nex,base_score,P)
# print(int(10**6*(1+10**8/(base_score+10**7))),base_score)
# print(*P)
# print(*B)
used_power = [0]*n
for i in range(n):
    if P[i] or i == 0:
        used_power[i] = 1

edges = []
for i in range(n):
    if used_power[i] == 0:
        continue
    for j in range(i):
        if used_power[j] == 0:
            continue
        edges.append([all_dist[i][j],i,j])
B = [0]*m
edges.sort()
uf = Unionfind(n)
for _,u,v in edges:
    if uf.same(u,v):
        continue
    uf.union(u,v)
    t = v
    while t != u:
        t,id = all_par[u][t]
        B[id] = 1

out()