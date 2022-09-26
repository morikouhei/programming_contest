import itertools
import sys
sys.setrecursionlimit(3*10**5)
n,m = map(int,input().split())
S = [input() for i in range(n)]

le = 0
for s in S:
    le += len(s)
T = set([input() for i in range(m)])
print(T)
dif = 16-le-(n-1)
# print(T,dif)
def dfs(l,ind,left,s):
    # print(l,ind,left,s)
    s += S[ind]
    if ind != n-1:
        s += "_"
    # print(s)
    if ind == n-1:
        if s not in T and 3 <= len(s) <= 16:
            print(s)
            exit()
        else:
            return
    for i in range(left+1):
        ss = s+"_"*i
        dfs(l,ind+1,left-i,ss)
    return 


for l in itertools.permutations(range(n),n):
    # print(l)
    dfs(l,0,dif,"")

print(-1)

