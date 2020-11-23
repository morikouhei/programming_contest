import sys
sys.setrecursionlimit(10**7)
a,b,c = map(int,input().split())
dp = {}

def dfs(x,y,z):
    if (x,y,z) in dp:
        return dp[(x,y,z)]
    if x >= 100 or y >= 100 or z >= 100:
        return 0
    s = x+y+z
    count = 0
    if x:
        count += x/s*(1+dfs(x+1,y,z))
    if y:
        count += y/s*(1+dfs(x,y+1,z))
    if z:
        count += z/s*(1+(dfs(x,y,z+1)))
    dp[(x,y,z)] = count
    return count

print(dfs(a,b,c))