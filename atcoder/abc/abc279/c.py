h,w = map(int,input().split())
S = [input() for i in range(h)]
T = [input() for i in range(h)]

S2 = []
for i in range(w):
    s = []
    for j in range(h):
        if S[j][i] == "#":
            s.append(1)
        else:
            s.append(0)
    S2.append(s)

T2 = []
for i in range(w):
    s = []
    for j in range(h):
        if T[j][i] == "#":
            s.append(1)
        else:
            s.append(0)
    T2.append(s)

if sorted(S2) == sorted(T2):
    print("Yes")
else:
    print("No")