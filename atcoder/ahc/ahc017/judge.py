import sys
from collections import deque

inf = 10**9
def dist_sum(n,g,used,day):

    dist_count = 0
    inf_case = []
    dist_if = 0
    no_inf_max = 0
    num0 = 0
    for i in range(n):
        dist = [inf]*n
        dist[i] = 0
        q = deque([i])
        while q:
            now = q.popleft()
            for nex,w,id in g[now]:
                if used[id]:
                    continue
                if dist[nex] > dist[now]+w:
                    dist[nex] = dist[now]+w
                    q.append(nex)
        dist_count += sum(dist)
        for d in dist:
            if d != inf:
                no_inf_max = max(no_inf_max,d)
                dist_if += d
        if inf not in dist:
            continue
        for j in range(i+1,n):
            if dist[j] == inf:
                
                inf_case.append([day,i,j])
    print(day,no_inf_max,len(inf_case))
    return dist_count/(n*(n-1)),inf_case,dist_if/(n*(n-1)-len(inf_case)*2)

def main(in_path,out_path,score_path):
    with open(in_path,"r") as f:
        n,m,d,k = [int(x) for x in f.readline().split()]
        UVW = [[int(x) for x in f.readline().split()] for i in range(m)]
        XY = [[int(x) for x in f.readline().split()] for i in range(n)]

    with open(out_path,"r") as f:
        R = [int(x) for x in f.readline().split()]



    ### check output R length and nums is under "k" for all days
    assert len(R) == m

    counts = [R.count(i) for i in range(1,d+1)]
    assert max(counts) <= k and sum(counts) == m

    g = [[] for i in range(n)]
    for i,(u,v,w) in enumerate(UVW):
        g[u-1].append([v-1,w,i])
        g[v-1].append([u-1,w,i])

    used = [0]*m
    base_count,_,_ = dist_sum(n,g,used,0)
    R_day = [[] for i in range(d)]
    for i,r in enumerate(R):
        R_day[r-1].append(i)

    scores = []
    scores_if = []
    inf_cases = []
    for day,r_day in enumerate(R_day,1):
        for r in r_day:
            used[r] = 1

        day_score,inf_case,day_score_if = dist_sum(n,g,used,day)
        inf_cases += inf_case
        scores.append(day_score-base_count)
        scores_if.append(day_score_if-base_count)

        for r in r_day:
            used[r] = 0

    score = sum(scores)*1000//(d*n*(n-1))
    score = int(sum(scores)*1000/(d))
    score_if = int(sum(scores_if)*1000/(d))

    print(f"score    = {score}")
    print(f"score_if = {score_if}")
    for s1,s2 in zip(scores,scores_if):
        print(s1,s2)
    if inf_cases:
        print(f"inf cases = {len(inf_cases)}")
        # for case in inf_cases:
        #     print(case)
        




if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])