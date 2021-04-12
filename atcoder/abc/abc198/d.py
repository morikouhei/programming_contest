import sys
sys.setrecursionlimit(3*10**5)
S = [input() for i in range(3)]

s = set()
not0 = set()

for i in S:
    s |= set(list(i))
    not0.add(i[0])

if len(s) > 10:
    print("UNSOLVABLE")
    exit()

L = list(s)
n = len(L)

def check(cand):
    num = []
    for i in range(3):
        count = 0
        for j in S[i]:
            count *= 10
            count += cand[L.index(j)]
        num.append(count)
    
    if num[0] + num[1] == num[2]:
        for i in num:
            print(i)
        exit()
    return
def dfs(cand):
    if len(cand) == n:
        check(cand)
        return -1
    l = len(cand)
    for i in range(10):
        if i in cand:
            continue
        if i == 0 and L[l] in not0:
            continue
        cand2 = cand.copy()
        cand2.append(i)
        dfs(cand2)

    return -1

ans = dfs([])
print("UNSOLVABLE")