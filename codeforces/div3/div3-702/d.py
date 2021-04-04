import sys
sys.setrecursionlimit(10**5)
t = int(input())

def dfs(l,r,d):
    if l == r:
        return
    m = 0
    ind = -1
    for i in range(l,r):
        if m < A[i]:
            m = A[i]
            ind = i
    ans[ind] = d
    dfs(l,ind,d+1)
    dfs(ind+1,r,d+1)
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    ans = [0]*n
    dfs(0,n,0)
    print(*ans)