import itertools
n,m = map(int,input().split())
S = [input() for i in range(n)]

for l in itertools.permutations(range(n),n):

    ok = 1
    for x,nx in zip(l,l[1:]):
        S1 = S[x]
        S2 = S[nx]

        dif = 0
        for s1,s2 in zip(S1,S2):
            if s1 != s2:
                dif += 1
        
        if dif != 1:
            ok = 0
    
    if ok:
        print("Yes")
        exit()
print("No")