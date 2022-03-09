import sys
sys.setrecursionlimit(2*10**6)
from functools import lru_cache

n,m = map(int,input().split())
mod = 10**9+7
invn = pow(n-1,mod-2,mod)

@lru_cache(None)
def dfs(x):
    if x == 0:
        return 0
    now = n
    count = n
    while now > 1:
        num = x//now
        nex = x//(num+1)
        count += dfs(num)*(now-nex)%mod
        count %= mod
        now = nex
    count *= invn
    count %= mod
    return count

print(dfs(m))