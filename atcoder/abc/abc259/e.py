n = int(input())
if n == 1:
    print(1)
    exit()
dic = {}
PE = []
for _ in range(n):
    m = int(input())
    pe = [list(map(int,input().split())) for j in range(m)]
    PE.append(pe)
    for p,e in pe:
        if p not in dic:
            dic[p] = [0]
        dic[p].append(e)

id = {k:i for i,k in enumerate(dic.keys(),1)}
for key in dic.keys():
    dic[key].sort()
ans = set()
mod = (1<<61)-1
mod2 = 10**9+7
for i in range(n):
    has = 1
    has2 = 1
    for p,e in PE[i]:
        if dic[p][-1] != e:
            continue
        dif = e-dic[p][-2]
        if dif == 0:
            continue
        has *= pow(p,dif,mod)
        has %= mod
        has2 *= pow(p,dif,mod2)
        has2 %= mod2
    ans.add((has,has2))
print(len(ans))
