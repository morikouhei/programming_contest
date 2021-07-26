import sys
sys.setrecursionlimit(2*10**5)

n,q = map(int,input().split())
A = list(map(int,input().split()))
e = [[] for i in range(n)]
for _ in range(q):
    x,y = [int(x)-1 for x in input().split()]
    e[x].append(y)

count = [0]*n

cand = [[] for i in range(10**4)]

def dfs(x,cum,l):
    if x == n:

        if cand[cum]:
            print(len(l))
            print(*l)
            print(len(cand[cum]))
            print(*cand[cum])
            exit()
        cand[cum] = l[:]
        return

    if count[x] == 0:
        for nex in e[x]:
            count[nex] += 1
        l.append(x+1)
        cum += A[x]
        dfs(x+1,cum,l)
        l.pop()
        cum -= A[x]
        for nex in e[x]:
            count[nex] -= 1
    dfs(x+1,cum,l)
    return 

dfs(0,0,[])


        