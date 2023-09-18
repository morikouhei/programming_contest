import sys
import time
import random
from math import exp
from heapq import heappop,heappush

TIME_LIM = 3.8
stime = time.time()


class Judge:

    def __init__(self,L,N,S,XY):

        self.N = N
        self.L = L
        self.S = S
        self.P = None
        self.count = 0
        self.MeasurementCost = 0
        self.PlacementCost = 0
        self.A = None
        self.f = None
        self.XY = XY
        self.DEBUG = 0


    def getInput(self):
        if self.DEBUG:
            self.A = [int(input()) for i in range(self.N)]
            self.f = [int(input()) for i in range(10**4)]

    
    def getP(self,P):
        self.P = P

        for p in P:
            print(*p)
        sys.stdout.flush()
        

    def ask_query(self,i,dx,dy,S=None):
        assert self.count < 10**4

        self.MeasurementCost += 100*(10+abs(dx)+abs(dy))
        print(f"{i} {dx} {dy}")
        sys.stdout.flush()

        if self.DEBUG:
            pos = self.A[i]
            x,y = self.XY[pos]
            nx,ny = (x+dx)%self.L,(y+dy)%self.L

            temp = self.P[nx][ny]

            temp += self.f[self.count]

            if temp < 0:
                temp = 0
            elif temp > 1000:
                temp = 1000

            # print(f"# return temp of {i} {dx} {dy} = {temp} A = {self.f[self.count]}")

           

        else:
            temp = int(input())

        self.count += 1
        
        if S == None:
            # print(f"# return temp = {temp}")
            return temp
        else:
            if temp == 0:
                while True:
                    rnd = random.gauss(0,S//2)
                    if rnd <= 0:
                        # print(f"# return temp = {temp}")
                        return temp+int(rnd)
            
            if temp == 1000:
                while True:
                    rnd = random.gauss(0,S//2)
                    if rnd >= 0:
                        # print(f"# return temp = {temp}")
                        return temp+int(rnd)
            # print(f"# return temp = {temp}")
            return temp


    def calc_score(self,wrong_count):

        L = self.L
        for i in range(L):
            for j in range(L):
                self.PlacementCost += (P[i][j]-P[(i+1)%L][j])**2
                self.PlacementCost += (P[i][j]-P[i][(j+1)%L])**2


        penalty = self.MeasurementCost + self.PlacementCost + 10**5

        return int(10**14*(0.8)**wrong_count/penalty) 


    def get_dist(self,i,j,set_temp,dxy):

        d1 = []

        x,y = XY[i]
        for dx,dy in dxy:
            nx,ny = x+dx*dif,y+dy*dif
            nx %= L
            ny %= L
            d1.append(set_temp.index(self.P[nx][ny]))

        d2 = []

        x,y = XY[j]
        for dx,dy in dxy:
            nx,ny = x+dx*dif,y+dy*dif
            nx %= L
            ny %= L
            d2.append(set_temp.index(self.P[nx][ny]))

        dist = 0
        for a,b in zip(d1,d2):
            dist += abs(a-b)

        return dist

    def answer_query(self,E,set_temp,dxy):

        assert len(E) == self.N

        print(-1,-1,-1)
        for e in E:
            print(e)
        sys.stdout.flush()

        if self.DEBUG:

            wrong_count = 0

            wrong_dist = []
            for e,a in zip(E,self.A):
                if e == a:
                    continue

                wrong_count += 1
                wrong_dist.append(f"# estimate is {e} true answer = {a} dist = {self.get_dist(e,a,set_temp,dxy)}¥n")



            score = self.calc_score(wrong_count)


            print(f"# Score = {score}")
            print(f"# L = {self.L} N = {self.N} S = {self.S}")
            print(f"# Number of wrong answers = {wrong_count}")
            print("".join(wrong_dist))
            print(f"# Placement cost = {self.PlacementCost}")
            print(f"# Measurement cost = {self.MeasurementCost}")
            print(f"# Measurement count = {self.count}")



L,N,S = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(N)]
inf = 10**10
if S > 25**2:
    inf2 = 10**6
else:
    inf2 = 10**5

judge = Judge(L,N,S,XY)
judge.getInput()


if S <= 9:
    set_temp = [500]
    for i in range(1,4):
        set_temp.append(500+3*S*i+i)
        set_temp.append(500-3*S*i-i)
    set_temp.sort()
    dxy = [[0,0],[0,1],[1,0]]
elif S <= 25:
    set_temp = [500]
    for i in range(1,4):
        set_temp.append(500+2*S*i+i)
        set_temp.append(500-2*S*i-i)
    set_temp.sort()
    dxy = [[0,0],[0,1],[1,0]]
elif S <= 64:
    # set_temp = [max(500-2*S-1,0),min(1000,500+2*S+1)]
    set_temp = [max(500-2*S-1,0),500,min(1000,500+2*S+1)]
    dxy = [[0,0],[0,1],[1,0],[0,-1],[-1,0]]

elif S < 20**2:
    set_temp = [max(int(500-S-1),0),min(1000,int(500+S+1))]
    # set_temp = [max(int(500-1.5*S-1),0),500,min(1000,int(500+1.5*S+1))]
    dxy = [[0,0],[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[0,2]]
else:
    set_temp = [max(int(500-0.7*S-1),0),min(1000,int(500+0.7*S+1))]
    # set_temp = [max(int(500-1.5*S-1),0),500,min(1000,int(500+1.5*S+1))]
    dxy = [[0,0],[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[0,2]]

temp_len = len(set_temp)
P = [[sum(set_temp)//temp_len]*L for i in range(L)]
temperature = []
dif = 3

ask_len = len(dxy)

for x,y in XY:

    for dx,dy in dxy:
        nx,ny = x+dx*dif,y+dy*dif
        nx %= L
        ny %= L

        rind = random.randint(0,temp_len-1)
        P[nx][ny] = set_temp[rind]



### climbing P

XY_use = [[[] for i in range(L)] for j in range(L)]
XY_temp = []
XY_climbing_list = set()
for i,(x,y) in enumerate(XY):
    temps = 0
    for j,(dx,dy) in enumerate(dxy):
        nx,ny = x+dx*dif,y+dy*dif
        nx %= L
        ny %= L

        XY_use[nx][ny].append([i,j])
        XY_climbing_list.add((nx,ny))
        temps += temp_len**j * set_temp.index(P[nx][ny])
    XY_temp.append(temps)

XY_climbing_len = len(XY_climbing_list)


dic = {}
def get_penalty(temp1,temp2):

    if temp1 > temp2:
        temp1,temp2 = temp2,temp1

    if (temp1,temp2) in dic:
        return dic[(temp1,temp2)]

    b1,b2 = temp1,temp2

    dist = 0
    t1 = []
    t2 = []
    for i in range(ask_len):
        temp1,m1 = divmod(temp1,temp_len)
        temp2,m2 = divmod(temp2,temp_len)
        t1.append(m1)
        t2.append(m2)
        dist += abs(m1-m2)

    if dist == 0:
        pena = 10**10
    elif dist == 1:
        pena = 10**8
    # else:
    #     pena = 0
    
    # print(f"# temp1 = {b1} temp2 = {b2} t1 = {t1} t2 = {t2} dist = {dist} temp = {temp1} pena = {pena}")
    elif dist <= 8:
        pena = 10**4 * dist
    else:
        pena = 0

    dic[(b1,b2)] = pena

    return pena
    

def get_id(temp1):

    num = 0
    for t in temp1:
        num *= 3
        num += t

    return num

def nC2(n):
    return n * (n-1) //2


def buildCost(x,y,temp):
    cost = 0

    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx = (x+dx)%L
        ny = (y+dy)%L

        cost += (temp-P[nx][ny])**2
    return cost



def check(P,freqs,base_score):
    score = 0
    for i in range(L):
        for j in range(L):
            score += buildCost(i,j,P[i][j])
 
 
    
    freqs_check = [0]*(temp_len**ask_len)
    for i,(x,y) in enumerate(XY):
        temps = 0
        for j,(dx,dy) in enumerate(dxy):
            nx,ny = x+dx*dif,y+dy*dif
            nx %= L
            ny %= L
            temps += temp_len**j * set_temp.index(P[nx][ny])
        freqs_check[temps] += 1
 
    
    assert freqs_check == freqs
 
    for i,b in enumerate(freqs):
        score += nC2(b) * inf

        if temp_len == 2 and S > 20**2:
            for j in range(ask_len):
                temp2 = i ^ (1<<j)

                score += freqs[temp2] * inf2 * b

    assert score == base_score,f"score = {score} base_score = {base_score}"
            
freqs = [0]*(temp_len**ask_len)
for i in range(N):
    freqs[XY_temp[i]] += 1

base_score = 0

XY_other_list = []
if True:
# if S < 20**2:
    for i,b in enumerate(freqs):
        base_score += nC2(b) * inf

        if temp_len == 2 and S > 20**2:
            for j in range(ask_len):
                temp2 = i ^ (1<<j)

                base_score += freqs[temp2] * inf2 * b


else:
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            base_score += get_penalty(XY_temp[i],XY_temp[j])

for i in range(L):
    for j in range(L):
        base_score += buildCost(i,j,P[i][j])
        if (i,j) not in XY_climbing_list:
            XY_other_list.append([i,j])

XY_other_len = len(XY_other_list)



rand_pos_list = []
for x,y in XY_climbing_list:

    for i in range(5):
        rand_pos_list.append([x,y,0])

for x,y in XY_other_list:

    for i in range(2):
        rand_pos_list.append([x,y,1])

# print("### start with ",base_score)

loop = 0
rand_len = len(rand_pos_list)
last_upd = -1
best_score = base_score
best_P = [p[:] for p in P]

START_TEMP = 1500
END_TEMP = 100
END_TIME = 3

TEMP = START_TEMP

if True:
# if S < 20**2:
    while True:
        
        loop += 1
        if loop % 5000 == 0:
            times = time.time() - stime
            if times> 3:
                break

            ratio = times / END_TIME
            TEMP = START_TEMP + (END_TEMP-START_TEMP) * ratio



        rind = random.randint(0,rand_len-1)

        x,y,types = rand_pos_list[rind]

        if types == 1:
            before_temp = P[x][y]
            new_score = base_score - buildCost(x,y,before_temp)*2
            new_temp = (P[(x+1)%L][y]+P[(x-1)%L][y]+P[x][(y+1)%L]+P[x][(y-1)%L])//4

            P[x][y] = new_temp
            new_score += buildCost(x,y,new_temp)*2

            if new_score >= base_score:
                P[x][y] = before_temp
            else:
                base_score = new_score
                # print(f"# update score to {base_score} time = {time.time()-stime}")
                # print(f"# new temp = {new_temp} at {x} {y}")

        else:

            before_temp = P[x][y]
            base_ind = set_temp.index(before_temp)

            new_ind = (base_ind+random.randint(1,temp_len-1))%temp_len
            new_temp = set_temp[new_ind]
            
            new_score = base_score - buildCost(x,y,before_temp)*2

            before_list = []
            new_list = []
            for i,j in XY_use[x][y]:
                temp = XY_temp[i]
                before_list.append([i,temp])
    
                new_score -= (freqs[temp]-1)*inf
                freqs[temp] -= 1
                if temp_len == 2 and S > 20**2:
                    for xj in range(ask_len):
        
                        temp2 = temp^(1<<xj)
                        new_score -= freqs[temp2] * inf2 * 2

                temp -= temp_len**j * base_ind
                temp += temp_len**j * new_ind
                new_score += freqs[temp]*inf
                freqs[temp] += 1
                XY_temp[i] = temp
                new_list.append([i,temp])

                if temp_len == 2 and S > 20**2:
                    for xj in range(ask_len):
            
                        temp2 = temp^(1<<xj)
                        new_score += freqs[temp2] * inf2 * 2
    
    
            P[x][y] = new_temp
            new_score += buildCost(x,y,new_temp)*2
                          
            if new_score <= base_score:
                base_score = new_score
                last_upd = loop
                # print(f"# update score to {base_score} time = {time.time()-stime}")
            else:
                # delta = base_score - new_score
                # prob = exp(delta/TEMP)

                # if prob > random.random():

                #     if best_score > base_score:
                #         best_score = base_score
                #         best_P = [p[:] for p in P]

                #     base_score = new_score
                #     last_upd = loop
                
                # else:

                P[x][y] = before_temp

                for i,temp in new_list:
                    freqs[temp] -= 1
                
                for i,temp in before_list:
                    freqs[temp] += 1
                    XY_temp[i] = temp
        

        # check(P,freqs,base_score)
        if loop - last_upd <= 5000:
            continue

        if best_score > base_score:
            best_score = base_score
            best_P = [p[:] for p in P]

        last_upd = loop
        x,y = random.randint(0,L-1),random.randint(0,L-1)

        for i in range(x-5,x+6):
            for j in range(y-5,y+6):
                ni = i%L
                nj = j%L
                if (ni,nj) not in XY_climbing_list or random.randint(0,1) == 1:
                    continue

                before_temp = P[ni][nj]
                base_ind = set_temp.index(before_temp)

                new_ind = (base_ind+random.randint(1,temp_len-1))%temp_len
                new_temp = set_temp[new_ind]

                base_score -= buildCost(ni,nj,before_temp)*2

                for si,sj in XY_use[ni][nj]:
                    temp = XY_temp[si]
 
                    base_score -= (freqs[temp]-1)*inf
                    freqs[temp] -= 1

                    if temp_len == 2 and S > 20**2:
                        for xj in range(ask_len):
    
                            temp2 = temp^(1<<xj)
                            base_score -= freqs[temp2] * inf2 * 2


                    temp -= temp_len**sj * base_ind
                    temp += temp_len**sj * new_ind
                    base_score += freqs[temp]*inf
                    freqs[temp] += 1
                    XY_temp[si] = temp

                    if temp_len == 2 and S > 20**2:
                        for xj in range(ask_len):
                
                            temp2 = temp^(1<<xj)
                            base_score += freqs[temp2] * inf2 * 2
    
                P[ni][nj] = new_temp
                base_score += buildCost(ni,nj,new_temp)*2

        # check(P,freqs,base_score)


print(f"# loop count = {loop}")
if base_score < best_score:
    best_score = base_score
    best_P = [p[:] for p in P]

P = [p[:] for p in best_P]

new_score = best_score
for x in range(L):
    for y in range(L):
        new_score -= buildCost(x,y,P[x][y])*2

for x in range(L):
    for y in range(L):
        if (x,y) in XY_climbing_list:
            continue
        new_temp = (P[(x+1)%L][y]+P[(x-1)%L][y]+P[x][(y+1)%L]+P[x][(y-1)%L])//4
        P[x][y] = new_temp

for x in range(L):
    for y in range(L):
        new_score += buildCost(x,y,P[x][y])*2


if new_score > best_score:
    P = [p[:] for p in best_P]
else:
    best_score = new_score

print(f"# build score = {best_score}",best_score//2)

build_score = 0
for x in range(L):
    for y in range(L):
        build_score += buildCost(x,y,P[x][y])
build_score //= 2

print("#", build_score,best_score//4)
XY_temp = []
for i,(x,y) in enumerate(XY):

    temps = []
    for dx,dy in dxy:
        nx,ny = x+dx*dif,y+dy*dif
        nx %= L
        ny %= L

        temps.append(P[nx][ny])
    XY_temp.append(temps)
    

judge.getP(P)

query_times = 10

def search_temp(i,dx,dy,dif,lim,S,temps):

    prob = [0]*temp_len
    ms = 0
    for j in range(lim):

        m = judge.ask_query(i,dx*dif,dy*dif,S)
        ms += m
        for ind,temp in enumerate(temps):

            for x in range(1,4)[::-1]:
                if abs(temp-m) > x*S:
                    prob[ind] += x
                    break
        

        
        sprob = prob[:]
        sprob.sort()

        for ind,temp in enumerate(temps):
            if prob[ind] == sprob[0] and sprob[1] - prob[ind] >= 6:
                return temp,j+1
        
    return ms//lim,lim

E = []
h = []
cands = []
query_num = 10**4
for i in range(N):

    temps = []
    query_list = []
    for dx,dy in dxy:
        
        ms,query = search_temp(i,dx,dy,dif,query_times,S,set_temp)
        temps.append(ms)
        query_list.append([ms*query,query])
        query_num -= query

    dist_min = 10**10
    e = -1
    for j in range(N):
        dist = 0
        for d1,d2 in zip(temps,XY_temp[j]):
            dist += abs(d1-d2)
        if dist < dist_min:
            dist_min = dist
            e = j
    heappush(h,[-dist_min,i])
    print(f"# e = {i} target={e} temps = {temps} best_temps = {XY_temp[e]}")
    cands.append([query_list,temps])
    E.append(e)

query_cost = (10**4-query_num)*2000

# print(f"# query_num = {10**5-query_num}")
while query_num > 0 and build_score //query_cost >= 10:

    dis,ind = heappop(h)
    if dis == 0:
        break
    query_list,temps = cands[ind]
    for j,(dx,dy) in enumerate(dxy):

        temp = temps[j]

        if temp in set_temp:
            continue
        
        ms_cost,query = query_list[j]
        
        if query_num:
            # print(f"# query_num = {query_num}")
            m = judge.ask_query(ind,dx*dif,dy*dif,S)
            query_num -= 1
            query_cost += 2000
            ms_cost += m
            query += 1
            temps[j] = ms_cost//query
            query_list[j] = [ms_cost,query]
    

    dist_min = 10**10
    e = -1
    for j in range(N):
        dist = 0
        for d1,d2 in zip(temps,XY_temp[j]):
            dist += abs(d1-d2)
        if dist < dist_min:
            dist_min = dist
            e = j
    E[ind] = e
    heappush(h,[-dist_min,ind])
    cands[ind] = [query_list,temps]


for i,e in enumerate(E):
    print(f"# e = {i} target={e} temps = {cands[i][1]} best_temps = {XY_temp[e]}")

judge.answer_query(E,set_temp,dxy)