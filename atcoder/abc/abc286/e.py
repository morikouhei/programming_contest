n = int(input())
A = list(map(int,input().split()))

dic = {"Y":1,"N":0}

S = [[dic[s] for s in input()] for i in range(n)]
inf = 10**10
dist = [[inf]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            dist[i][j] = 0
        if S[i][j]:
            dist[i][j] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != inf and dist[k][j] != inf:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])



gain = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if S[i][j]:
            gain[i][j] = A[i]+A[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] + dist[k][j] != dist[i][j]:
                continue

            gain[i][j] = max(gain[i][j], gain[i][k] + gain[k][j]-A[k])




q = int(input())
UV = [[int(x)-1 for x in input().split()] for i in range(q)]
for u,v in UV:
    if dist[u][v] == inf:
        print("Impossible")
    else:
        print(dist[u][v],gain[u][v])