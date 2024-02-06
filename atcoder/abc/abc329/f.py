n,q = map(int,input().split())
C = list(map(int,input().split()))

sets = [set() for i in range(n)]
for i,c in enumerate(C):
    sets[i].add(c)


AB = [[int(x)-1 for x in input().split()] for i in range(q)]


for a,b in AB:

    if len(sets[a]) > len(sets[b]):
        sets[a],sets[b] = sets[b],sets[a]

    for x in sets[a]:
        sets[b].add(x)
    sets[a] = set()

    print(len(sets[b]))