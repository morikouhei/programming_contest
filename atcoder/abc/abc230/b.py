S = input()
T = "oxx"*100
for i in range(3):
    ok = 1
    for j,s in enumerate(S):
        if s != T[i+j]:
            ok = 0
    if ok:
        print("Yes")
        exit()
print("No")