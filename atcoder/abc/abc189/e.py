import sys
input = sys.stdin.readline

n = int(input())
xy = [tuple(map(int,input().split())) for i in range(n)]
m = int(input())
op = [list(map(int,input().split())) for i in range(m)]
q = int(input())
Q = [[] for i in range(m+1)]
for i in range(q):
    a,b = map(int,input().split())
    Q[a].append((b-1,i))

X = [1,0,0]
Y = [0,1,0]

ans = [0]*q
for i in range(m+1):
    for b,ind in Q[i]:

        x = X[0]*xy[b][0]+X[1]*xy[b][1]+X[2]
        y = Y[0]*xy[b][0]+Y[1]*xy[b][1]+Y[2]
        ans[ind] = [x,y]
    if i == m:
        break
    if op[i][0] == 1:
        X,Y = Y, [-X[i] for i in range(3)]
    elif op[i][0] == 2:
        X,Y = [-Y[i] for i in range(3)],X

    elif op[i][0] == 3:
        p = op[i][1]
        X = [-X[0],-X[1],2*p-X[2]]
    else:
        p = op[i][1]
        Y = [-Y[0],-Y[1],2*p-Y[2]]

for i in ans:
    print(*i)