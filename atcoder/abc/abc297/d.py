import sys
sys.setrecursionlimit(3*10**5)
a,b = map(int,input().split())

def dfs(a,b):
    if b > a:
        a,b = b,a

    if a == b:
        return 0

    na = a%b

    if na == 0:
        return a//b-1
    
    count = (a-na)//b

    count += dfs(b,na)

    return count

print(dfs(a,b))