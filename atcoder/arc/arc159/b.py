import math
import sys
sys.setrecursionlimit(3*10**6)
def dfs(a,b):
    
    if a*b == 0:
        return 0

    g = math.gcd(a,b)
    a //= g
    b //= g
    dif = a-b

    nex = 10**20
    for i in range(1,int(dif**0.5)+1):

        if dif%i:
            continue


        ni = i
        if ni > 1:
            if a%ni == b%ni:
                nex = min(nex,a%ni)
        
        ni = dif//i
        if ni > 1:
            if a%ni == b%ni:
                nex = min(nex,a%ni)
    
    if nex == 10**20:
        return b
    else:
        count = nex + dfs(a-nex,b-nex)

    return count


# def dfs_greedy(a,b,lg):
    
#     if a*b == 0:
#         return 0

#     g = math.gcd(a,b)
#     if lg != g:
#         print(a,b,g,lg,a//g,b//g)
    
#     ans = 1 + dfs_greedy(a-g,b-g,g)

#     return ans
a,b = map(int,input().split())
if b > a:
    a,b = b,a
print(dfs(a,b))
# print(dfs_greedy(a,b,-1))