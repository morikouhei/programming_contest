S = input()

B = []
for i,s in enumerate(S):
    if s == "B":
        B.append(i)

if B[0]%2 == B[1]%2:
    print("No")
    exit()


l = []
for s in S:
    if s == "K" or s == "R":
        l.append(s)

if "".join(l) == "RKR":
    print("Yes")
else:
    print("No")