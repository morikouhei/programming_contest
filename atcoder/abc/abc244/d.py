import itertools
S = input().split()
T = input().split()

ss = sorted(S)
tt = sorted(T)
if ss != tt:
    print("No")
    exit()


if S == T:
    print("Yes")
    exit()
    
for l in itertools.permutations(range(3),3):

    sta = S[:]
    for i,j in enumerate(l,1):
        if j == 0:
            sta[1],sta[2] = sta[2],sta[1]
        elif j == 1:
            sta[0],sta[2] = sta[2],sta[0]
        else:
            sta[0],sta[1] = sta[1],sta[0]
        if sta == T and i == 2:
            print("Yes")
            exit()
print("No")