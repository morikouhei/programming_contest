import sys
sys.setrecursionlimit(2*10++5)
n,x,y = map(int,input().split())

def dfs(l,r,b):
    if l == 1:
        return b

    nr = 0
    nb = 0
    nb += b*y
    nr += b
    nr += r
    nr += r*x
    nb += r*x*y

    ans = dfs(l-1,nr,nb)

    return ans
print(dfs(n,1,0))