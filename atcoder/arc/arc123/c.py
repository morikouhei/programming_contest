import sys
sys.setrecursionlimit(2*10**5)
dic = {0:0}

def dfs(x):
    if x in dic:
        return dic[x]
    cand = 6
    for i in range(1,6):
        for j in range(i,3*i+1):
            if (x-j)%10 or x < j:
                continue
            if dfs((x-j)//10) <= i:
                cand = min(cand,i)
    dic[x] = cand

    return cand
def solve():
    n = int(input())
    print(dfs(n))
T = int(input())
for _ in range(T):
    solve()