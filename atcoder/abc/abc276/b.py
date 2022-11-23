n,m = map(int,input().split())
e = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    e[a-1].append(b)
    e[b-1].append(a)

for i in range(n):
    l = [len(e[i])] + sorted(e[i])
    print(*l)