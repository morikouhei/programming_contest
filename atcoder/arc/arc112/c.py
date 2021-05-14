n = int(input())
P = list(map(int,input().split()))
e = [[] for i in range(n)]
for i,p in enumerate(P,1):
    p -= 1
    e[i].append(p)
    e[p].append(i)

