import sys
sys.setrecursionlimit(2*10**7)
n = int(input())

A = [list(map(int,input().split())) for i in range(2*n-1)]

ans = 0
bit = (1<<(2*n))-1
dic = {}
def dfs(x,num):
    if x == bit:

        global ans
        ans = max(ans,num)
        return

    for i in range(2*n):
        if x >> i & 1:
            continue
        cand = x | 1<<i
        nex = i
        break

    for j in range(nex+1,2*n):
        if cand >> j & 1:
            continue
        nnum = num ^ A[nex][j-nex-1]
        dfs(cand|1<<j,nnum)
 
    return 

dfs(0,0)
print(ans)

