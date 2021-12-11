import sys
input = sys.stdin.readline
from heapq import heappush, heappop

class mincostflow:

    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost

    def __init__(self, n):
        self.n = n
        self.pos = []
        self.g = [[] for i in range(n)]

    def add_edge(self, from_, to, cap, cost):
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_])-1, 0, -cost))
        return m

    def get_edge(self, i):
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        result = []
        for i in range(len(self.pos)):
            result.append(self.get_edge(i))
        return result

    def slope(self, s, t, flow_limit=10**20, inf=10**20):
        dual = [0]*self.n
        dist = [inf]*self.n
        pv = [-1]*self.n
        pe = [-1]*self.n
        vis = [False]*self.n

        def _dual_ref():
            nonlocal dual, dist, pv, pe, vis
            dist = [inf]*self.n
            pv = [-1]*self.n
            pe = [-1]*self.n
            vis = [False]*self.n

            que = [(0,s)]
            dist[s] = 0
            while que:
                _,v = heappop(que)
                if vis[v]:
                    continue
                vis[v] = True

                if v == t:
                    break
                for i in range(len(self.g[v])):
                    e = self.g[v][i]
                    if vis[e.to] or e.cap == 0:
                        continue
                    cost = e.cost - dual[e.to] + dual[v]
                    if dist[e.to] > dist[v] + cost:
                        dist[e.to] = dist[v] + cost
                        pv[e.to] = v
                        pe[e.to] = i
                        heappush(que, (dist[e.to],e.to))
            if not vis[t]:
                return False

            for v in range(self.n):
                if not vis[v]:
                    continue
                dual[v] -= dist[t] - dist[v]
            return True
        
        flow = 0
        cost = 0
        prev_cost = -1

        result = [(flow, cost)]
        while flow < flow_limit:
            if not _dual_ref():
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[pv[v]][pe[v]].cap)
                v = pv[v]

            v = t
            while v != s:
                e = self.g[pv[v]][pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = pv[v]
            
            d = -dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result

    def flow(self, s, t, flow_limit=10**20):
        return self.slope(s, t, flow_limit)[-1]

# assign random tasks to team member 1.
import sys
import random
from heapq import heappush, heappop
# Prior information
n, m, k, r = list(map(int, input().split()))
task_difficulty = []
for i in range(n):
    task_difficulty.append(list(map(int, input().split())))
task_dependency = [[] for _ in range(n)]
par = [0]*n
for i in range(r):
    u,v = [int(x)-1 for x in input().split()]
    task_dependency[u].append(v)
    par[v] += 1

path_length = [0]*n
for i in range(n)[::-1]:
    for nex in task_dependency[i]:
        path_length[i] = max(path_length[i],path_length[nex]+sum(task_difficulty[nex])//k)
# -1: not started
#  0: started
#  1: completed
task_status = [-1] * n
task_list = []

for i in range(n):
    if par[i]:
        continue
    heappush(task_list,[-path_length[i],-len(task_dependency[i]),-sum(task_difficulty[i]),i])

# -1: not assigned
#  k: assigned task k (1 <= k <= N)
member_status = [-1] * m
start_day = [-1] * m
member_ability = [[1]*k for i in range(m)]

def member_update(mid,taskid,day):
    done = day-start_day[mid]-1
    for i in range(k):
        member_ability[mid][i] = max(member_ability[mid][i],task_difficulty[taskid][i]-done)

def need_day(mid,taskid):
    days = 1
    for i in range(k):
        days = max(days, task_difficulty[taskid][i]-member_ability[mid][i])

    return days

def task_assign(members,jobs):
    
    lm = len(members)
    lj = len(jobs)
    s = lm+lj
    t = s+1
    member_job = [-1]*lm

    flow = mincostflow(t+1)
    for i in range(lj):
        flow.add_edge(s,i,1,0)
    for i in range(lm):
        flow.add_edge(lj+i,t,1,0)

    for i in range(lj):
        taskid = jobs[i]
        for j in range(lm):
            mid = members[j]
            day = need_day(mid,taskid)
            flow.add_edge(i,lj+j,1,day)

    flow.flow(s,t,lj)
    for e in flow.edges():
        if e.from_ == s or e.to == t or e.flow == 0:
            continue
        member_job[e.to-lj] = jobs[e.from_]

    return member_job

for i in range(2000):

    jobs = []
    if i:
        next_member = []
        for j in range(m):
            if member_status[j] != -1:
                continue
            next_member.append(j)
        next_job = []
        while task_list and len(next_job) < len(next_member):
            _,_,_,njob = heappop(task_list)
            next_job.append(njob)
        
        if next_job != [] and next_member != []:
            member_job = task_assign(next_member,next_job)
            for j in range(len(member_job)):
                if member_job[j] == -1:
                    continue
                njob = member_job[j]
                mid = next_member[j]
                jobs.append(mid+1)
                jobs.append(njob+1)
                member_status[mid] = njob
                start_day[mid] = i
                task_status[njob] = 0
                

    else:
        
        for j in range(m):
            if member_status[j] != -1:
                continue
            if task_list:
                _,_,_,njob = heappop(task_list)
                start_day[j] = i
                jobs.append(j+1)
                jobs.append(njob+1)
                task_status[njob] = 0
                member_status[j] = njob
    print(len(jobs)//2,*jobs)

    # After the output, you have to flush Standard Output
    sys.stdout.flush()
    temp = list(map(int, input().split()))
    if len(temp) == 1:
        if temp[0] == -1:
            # elapsed days == 2000, or all the tasks have been completed
            exit()
        else:
            # no change in state
            pass
    else:
        # one task has been completed
        for j in temp[1:]:
            j -= 1
            now = member_status[j]
            for nex in task_dependency[now]:
                par[nex] -= 1
                if par[nex] == 0:
                    heappush(task_list,[-path_length[nex],-len(task_dependency[nex]),-sum(task_difficulty[nex]),nex])
            task_status[now] = 1
            member_status[j] = -1
            member_update(j,now,i)
            start_day[j] = -1
