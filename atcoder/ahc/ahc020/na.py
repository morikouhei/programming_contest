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
TIME_LIM = 1.8

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
house_to_power_dist = [[] for i in range(k)]
for i,(x,y) in enumerate(XY):
    power_to_house = []
    for j,(a,b) in enumerate(AB):
        d = get_dis(a,b,x,y)
        d = get_p_int(d)
        power_to_house.append([d,j])
        house_to_power_dist[j].append([d,i])
    power_to_house.sort()
    power_to_house_dist.append(power_to_house)

for i in range(k):
    house_to_power_dist[i].sort()



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

times = 0
def clime_update(s,p_nex,base_score,P,B,used_power):
    p_target = bsearch_left_power_to_house(s,p_nex)
    p_nex = power_to_house_dist[s][p_target][0]
    if p_nex <= P[s]:
        return base_score,P,B,used_power

    new_P = [0]*n
    new_B = [0]*m
    new_used_power = [0]*n
    new_used_power[s] = 1
    new_used_power[0] = 1

    new_P[s] = p_nex

    use_house = [0]*k
    for nd,id in power_to_house_dist[s]:
        if nd <= p_nex:
            use_house[id] = 1
        else:
            break

    dist_list = []
    for i in range(k):
        if use_house[i]:
            continue

        # ind = random.randint(0,8)
        ind = 0
        if ind < 4:
            d,id = house_to_power_dist[i][0]
        elif ind < 7:
            d,id = house_to_power_dist[i][1]
        elif ind < 9:
            d,id = house_to_power_dist[i][2]
        else:
            d,id = house_to_power_dist[i][3]

        dist_list.append([-d,i,id])

    dist_list.sort()

    for d,house_id,power_id in dist_list:
        if use_house[house_id]:
            continue
        d *= -1
        
        new_P[power_id] = d
        new_used_power[power_id] = 1

        for i,(nd,id) in enumerate(power_to_house_dist[power_id]):
            if nd <= d:
                use_house[id] = 1
            else:
                break

    edges = []
    for i in range(n):
        if new_used_power[i] == 0:
            continue
        for j in range(i):
            if new_used_power[j] == 0:
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
            new_B[id] = 1
        
        
    new_score = 0
    for p in new_P:
        new_score += p**2

    for i in range(m):
        if new_B[i]:
            new_score += UVW[i][2]
    
    if new_score <= base_score:
        return new_score,new_P,new_B,new_used_power
    else:
        return base_score,P,B,used_power


use_P = []
for i in range(n):
    if P[i]:
        use_P.append(i)

le = len(use_P)
while time.time() - stime <= TIME_LIM:
    times += 1
    s = use_P[random.randint(0,le-1)]
    p_max = min(P[s]+1000,5000,power_to_house_dist[s][-1][0])

    p_nex = random.randint(P[s]+1,p_max)

    base_score,P,B,used_power = clime_update(s,p_nex,base_score,P,B,used_power)
# print(times)
print(int(10**6*(1+10**8/(base_score+10**7))),base_score)
out()