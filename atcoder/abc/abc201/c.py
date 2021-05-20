S = input()
x = S.count("x")
o = S.count("o")
if o > 4:
    print(0)
    exit()

cand = []
need = []
for i in range(10):
    if S[i] == "o":
        need.append(i)
        cand.append(i)
    if S[i] == "?":
        cand.append(i)
ans = 0
for i in range(len(cand)):
    for j in range(len(cand)):
        for k in range(len(cand)):
            for t in range(len(cand)):
                a = [cand[i],cand[j],cand[k],cand[t]]
                check = True
                for x in need:
                    if x not in a:
                        check = False
                if check:
                    ans += 1
print(ans)