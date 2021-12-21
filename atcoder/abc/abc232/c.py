import itertools
n,m = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(m)]
CD = [list(map(int,input().split())) for i in range(m)]


for l in itertools.permutations(range(1,n+1),n):
    ok = 1
    for a,b in AB:
        if [l[a-1],l[b-1]] in CD or [l[b-1],l[a-1]] in CD:
            continue
        ok = 0
        break
    if ok:
        print("Yes")
        exit()
print("No")