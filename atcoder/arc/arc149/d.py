from collections import deque

n,m = map(int,input().split())
X = list(map(int,input().split()))
D = list(map(int,input().split()))

M = 10**6+5

e = [[] for i in range(M)]

status = [0]*M
goal = [0]*M
q = deque([i for i in range(1,M)])

def merge(turn,num,leave):

    dels = []
    for i in range(leave+1):
        if turn:
            dels.append(q.pop())
        else:
            dels.append(q.popleft())

    status[dels.pop()] = num

    adds = []
    for i in range(leave):
        if turn:
            adds.append(q.pop())
        else:
            adds.append(q.popleft())
    
    for ad,de in zip(adds[::-1],dels):
        e[ad].append(de)
    
        if turn:
            q.append(ad)
        else:
            q.appendleft(ad)

l = 1
r = M-1
turn = 0

for i,d in enumerate(D,1):

    if not q:
        break
    nl = abs(l-d)
    nr = abs(r-d)

    if l > d or r < d:
        if nl > nr:
            turn ^= 1
        l,r = min(nl,nr),max(nl,nr)
        continue
    
    leave = d-l
    if leave > r-l-leave:
        turn ^= 1
        leave = r-l-leave

    merge(turn,i,leave)
    l,r = 1,max(nl,nr)


def calc(x,p,go):

    que = [x]
    while que:
        now = que.pop()
        goal[now] = go
        for nex in e[now]:
            status[nex] = status[now]*p
            que.append(nex)

for i in range(M):
    if status[i]:
        calc(i,1,1)

q = list(q)
if turn:
    q = q[::-1]

for i,ind in enumerate(q,l):
    if turn:
        out = -i
    else:
        out = i
    status[ind] = out
    calc(ind,-1,0)

for x in X:
    go,pos = goal[x],status[x]
    if go:
        print("Yes",pos)
    else:
        print("No",pos)

