import random
import time

LIM_time = 12
base_size = 4
frequency_num = 100
target_dis = 60
m,eps = input().split()
m = int(m)
eps = int(eps[2:])

stime = time.time()
def size(x):
    return x*(x-1)//2



def sequence_to_table(sequence,n):

    table = [[0]*n for i in range(n)]
    now = 0
    for i in range(n):
        for j in range(i+1,n):
            table[i][j] = table[j][i] = sequence[now]
            now += 1
    return table

def table_to_edges(table,n):
    edges = [[0,i] for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if table[i][j]:
                edges[i][0] += 1
                edges[j][0] += 1
    
    edges.sort()
    return [edge[0] for edge in edges]

def table_to_sequence(table,n):

    edges = [[0,i] for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if table[i][j]:
                edges[i][0] += 1
                edges[j][0] += 1
    
    edges.sort()

    new_table = [[0]*n for i in range(n)]
    for i in range(n):
        x = edges[i][1]
        for j in range(i+1,n):
            y = edges[j][1]
            new_table[i][j] = new_table[j][i] = table[x][y]

    sequence = []
    for i in range(n):
        for j in range(i+1,n):
            sequence.append(new_table[i][j])

    return sequence


def make_frequent_graph(graph,n):

    frequency_g = [[0]*(n+1) for i in range(n)]

    base_dist = [0]*n

    now = 0
    
    for i in range(n):
        for j in range(i+1,n):
            g = graph[now]
            base_dist[i] += g
            base_dist[j] += g
            now += 1
    temp_dist = [0]*n
    graph_temp = [-1 if g else 1 for g in graph]
    for _ in range(frequency_num):

        for i in range(n):
            temp_dist[i] = base_dist[i]

        now = 0
        for i in range(n):
            for j in range(i+1,n):
                if random.randint(1,100) <= eps:
                    
                    temp_dist[i] += graph_temp[now]
                    temp_dist[j] += graph_temp[now]
                now += 1

        temp_dist.sort()
        for i,temp in enumerate(temp_dist):
            frequency_g[i][temp] += 1
        
    return frequency_g


def make_frequent_graph_all(graph,n):

    frequency = [[[0]*(n+1) for i in range(n)] for j in range(m)]

    base_dist_all = []
    for gra in graph:
        base_dist = [0]*n

        now = 0
        
        for i in range(n):
            for j in range(i+1,n):
                g = gra[now]
                base_dist[i] += g
                base_dist[j] += g
                now += 1
        base_dist_all.append(base_dist)
    temp_dist = [0]*n
    graph_temp_all = []
    for gra in graph:
        graph_temp = [-1 if g else 1 for g in gra]
        graph_temp_all.append(graph_temp)

    while time.time()-stime <= 4:
        
        for id,graph_temp in enumerate(graph_temp_all):

            for i in range(n):
                temp_dist[i] = base_dist_all[id][i]

            now = 0
            for i in range(n):
                for j in range(i+1,n):
                    if random.randint(1,100) <= eps:
                        temp_dist[i] += graph_temp[now]
                        temp_dist[j] += graph_temp[now]
                    now += 1

            temp_dist.sort()
            for i,temp in enumerate(temp_dist):
                frequency[id][i][temp] += 1
        
    return frequency

def calc_score(h_edges,frequency_g,n):

    count = 0
    for i,h in enumerate(h_edges):
        for j in range(n+1):
            if j > h:
                x = frequency_g[i][j]
                count += x * (j-h)
            else:
                x = frequency_g[i][j]
                count += x * (h-j)
    return count

def predict(graph,n):
    # frequency = []
    # for g in graph:
    #     frequency.append(make_frequent_graph(g,n))
    frequency = make_frequent_graph_all(graph,n)

    

    for _ in range(100):
        h = list(map(int,input()))
        h_table = sequence_to_table(h,n)
        h_edges = table_to_edges(h_table,n)
        ans = 0
        score = 10**10
        for i in range(m):
            temp_score = calc_score(h_edges,frequency[i],n)
            if temp_score < score:
                score = temp_score
                ans = i

        print(ans)

def make_graph_0(m):
    if m <= 11:
        n = 4
    elif m <= 31:
        n = 5
    else:
        n = 6

    s = size(n)
    alls = set()
    graph = []
    for i in range(1<<s):

        count = [0]*n
        now = 0
        temp = []
        for j in range(n):
            for k in range(j+1,n):
                if i >> now & 1:
                    temp.append(1)
                    count[j] += 1
                    count[k] += 1
                else:
                    temp.append(0)
                now += 1
            
        st = "".join([str(x) for x in sorted(count)])
        if st in alls:
            continue
        graph.append(temp)

        alls.add(st)
    return n,graph[:m]


def make_graph(m):
    if eps <= 1:
        return make_graph_0(m)
    
    if eps <= 3:
        target_dis = 20
    elif eps <= 7:
        target_dis = 30
    elif eps <= 12:
        target_dis = 50
    else:
        target_dis = 80
    
    for i in range(1,100):
        g_size = i*(i-1)
        if g_size >= (m-1)*target_dis:
            n = i
            while g_size >= (m-1)*(target_dis+2):
                target_dis += 2
            if eps <= 20:
                break
            # break
    # print(target_dis)

    seq_size = size(n)
    graph = []
    graph.append([0]*seq_size)

    base_table = [[0]*n for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            base_table[i][j] = base_table[j][i] = 1
            count += 2

            if count%target_dis == 0:
                graph.append(table_to_sequence(base_table,n))
    
    return n,graph[:m]


n,graph = make_graph(m)

print(n)
for g in graph:
    print(*g,sep="")
predict(graph,n)