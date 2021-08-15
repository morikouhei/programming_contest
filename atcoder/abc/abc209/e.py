from collections import deque
n = int(input())
S = [input() for i in range(n)]

lis = set()
for s in S:
    lis.add(s[:3])
    lis.add(s[-3:])
dic = {x:i for i,x in enumerate(sorted(lis))}

n = len(lis)
e = [[] for i in range(n)]
count = [0]*n
for s in S:
    a = dic[s[:3]]
    b = dic[s[-3:]]
    e[b].append(a)
    count[a] += 1


battle = [0]*n
q = deque()
for i in range(n):
    if count[i]:
        continue
    q.append(i)
    battle[i] = -1

while q:
    now = q.popleft()
    for nex in e[now]:
        if battle[nex]:
            continue
        if battle[now] == -1:
            battle[nex] = 1
            q.append(nex)

        else:
            count[nex] -= 1
            if count[nex] == 0:
                battle[nex] = -1
                q.append(nex)
        

for s in S:
    win = battle[dic[s[-3:]]]
    if win == -1:
        print("Takahashi")
    elif win == 0:
        print("Draw")
    else:
        print("Aoki")
