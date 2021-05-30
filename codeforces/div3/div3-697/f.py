from copy import deepcopy

def solve():
    n = int(input())
    A = [input() for i in range(n)]
    nA = []
    for a in A:
        l = [int(i) for i in a]
        nA.append(l)
    _ = input()
    B = [input() for i in range(n)]
    nB = []
    for a in B:
        l = [int(i) for i in a]
        nB.append(l)
    cA = deepcopy(nA)
    def check(cA,B):
        for i in range(1,n):
            if cA[i][0] == B[i][0]:
                continue
            for j in range(n):
                cA[i][j] ^= 1
    
        for i in range(1,n):
            if cA[0][i] == B[0][i]:
                continue
            for j in range(n):
                cA[j][i] ^= 1
        for i in range(n):
            for j in range(n):
                if cA[i][j] != B[i][j]:
                    return 0
        return 1
    if check(cA,nB):
        return "YES"
    cA = deepcopy(nA)
    for i in range(n):
        cA[0][i] ^= 1
    if check(cA,nB):
        return "YES"
    cA  = deepcopy(nA)
    for i in range(n):
        cA[i][0] ^= 1
    if check(cA,nB):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)