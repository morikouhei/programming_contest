import sys
sys.setrecursionlimit(3*10**5)

n = int(input())
C = list(map(int,input().split()))

e = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    e[a].append(b)
    e[b].append(a)

ans = []
count = [0]*(10**5+5)

def dfs(x,p):

    if count[C[x]] == 0:
        ans.append(x)
    count[C[x]] += 1
    for i in e[x]:
        if i == p:
            continue
        dfs(i,x)
    count[C[x]] -= 1

dfs(0,-1)
ans.sort()
for i in ans:
    print(i+1)
