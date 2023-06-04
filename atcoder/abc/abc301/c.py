S = input()
T = input()

numS = [0]*27
numT = [0]*27
for s in S:
    if s == "@":
        numS[-1] += 1
    else:
        numS[ord(s) -ord("a")] += 1

for s in T:
    if s == "@":
        numT[-1] += 1
    else:
        numT[ord(s) -ord("a")] += 1
        

for i in range(26):
    s = chr(ord("a")+i)

    if numS[i] == numT[i]:
        continue
    if s not in "atcoder":
        print("No")
        exit()

    a,b = numS[i],numT[i]
    if a > b:
        if numT[-1] < a-b:
            print("No")
            exit()
        numT[-1] -= a-b
    else:
        if numS[-1] < b-a:
            print("No")
            exit()
        numS[-1] -= b-a
print("Yes")