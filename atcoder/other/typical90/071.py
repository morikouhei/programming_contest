from collections import deque
import sys
sys.setrecursionlimit(2*10**5)
input = sys.stdin.readline

n,m,k = map(int,input().split())
ind = [0]*n
e = [[] for i in range(n)]
for i in range(m):
    a,b = [int(x)-1 for x in input().split()]
    e[a].append(b)
    ind[b] += 1

perm = [-1]*n
st = []
ans = []

def dfs(dep):
    if dep == n:
        global ans
        ans.append(perm[:])
        return True
    if not st:
        return False
    
    for i in range(len(st))[::-1]:
        if len(ans) == k:
            break
        x = st[i]
        del st[i]
        for j in e[x]:
            ind[j] -= 1
            if ind[j] == 0:
                st.append(j)
        perm[dep] = x+1
        ok = dfs(dep+1)
        if not ok:
            return False
        for j in e[x]:
            if ind[j] == 0:
                st.pop()
            ind[j] += 1
        st.insert(i,x)
    return True

for i in range(n):
    if ind[i] == 0:
        st.append(i)

dfs(0)
if len(ans) != k:
    print(-1)
    exit()
for x in ans:
    print(*x)