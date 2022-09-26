import sys
sys.setrecursionlimit(2*10**6)
n,k = map(int,input().split())
A = list(map(int,input().split()))

dic = {}

def dfs(stone):

    if stone in dic:
        return dic[stone]

    cand = stone    
    for a in A:
        if a <= stone:
            cand = min(cand,dfs(stone-a))
    dic[stone] = stone-cand

    return dic[stone]

print(dfs(n))