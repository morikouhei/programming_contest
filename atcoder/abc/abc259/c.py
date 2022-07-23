S = input()
T = input()

lS = []

for s in S:
    if lS and lS[-1][0] == s:
        lS[-1][1] += 1
    else:
        lS.append([s,1])

lT = []
for s in T:
    if lT and lT[-1][0] == s:
        lT[-1][1] += 1
    else:
        lT.append([s,1])

if len(lS) != len(lT):
    print("No")
    exit()

for i in range(len(lS)):
    s,ns = lS[i]
    t,nt = lT[i]

    if s != t:
        print("No")
        exit()
    if ns > nt or (ns != nt and ns == 1):
        print("No")
        exit()
print("Yes")