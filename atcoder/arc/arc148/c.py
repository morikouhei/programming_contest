n,q = map(int,input().split())

edges = [0]*n
P = [-1]+[int(x)-1 for x in input().split()]
for p in P[1:]:
    edges[p] += 1

for _ in range(q):
    l = [int(x)-1 for x in input().split()]
    ans = 0
    used = set()

    for v in l[1:]:
        if P[v] in used:
            ans -= 2
        ans += edges[v]+1
        used.add(v)
    print(ans)
    