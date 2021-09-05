from collections import deque
n,m = map(int,input().split())

lis = [[] for i in range(n)]
cand = []
for i in range(m):
    k = int(input())
    cand.append(list(map(int,input().split()))[::-1])

for i in range(m):
    x = cand[i].pop()
    lis[x-1].append(i)

q = deque()
for i in range(n):
    if len(lis[i]) == 2:
        q.append((lis[i][0],lis[i][1]))
        lis[i] = []

while q:
    x,y = q.popleft()
    if cand[x]:
        a = cand[x].pop()-1
        lis[a].append(x)
        if len(lis[a]) == 2:
            q.append((lis[a][0],lis[a][1]))
            lis[a] = []
    if cand[y]:
        a = cand[y].pop()-1
        lis[a].append(y)
        if len(lis[a]) == 2:
            q.append((lis[a][0],lis[a][1]))
            lis[a] = []

for c in cand:
    if c != []:
        print("No")
        exit()
print("Yes")