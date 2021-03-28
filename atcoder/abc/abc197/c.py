import sys
sys.setrecursionlimit(4*10**6)
n = int(input())
A = list(map(int,input().split()))

dic = {}
def dfs(x,num,xor):

    if x == n:
        return num^xor
    if (x,num,xor) in dic:
        return dic[(x,num,xor)]
    ans = 10**30
    a = A[x]
    ans = min(ans,dfs(x+1,a|num,xor))
    ans = min(ans,dfs(x+1,a,xor^num))

    dic[(x,num,xor)] = ans
    return ans

print(dfs(0,0,0))