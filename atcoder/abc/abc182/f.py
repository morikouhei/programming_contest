n,X = map(int,input().split())
A = list(map(int,input().split()))
from functools import lru_cache

@lru_cache()
def dfs(x,i):
    if i == n-1:
        return 1
    a,b = A[i],A[i+1]
    if x%b == 0:
        return dfs(x,i+1)
    x -= x%b
    return dfs(x,i+1)+dfs(x+b,i+1)

print(dfs(X,0))
    