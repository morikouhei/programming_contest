n,m = map(int,input().split())

ans = []

def dfs(x,l):
    if len(l) == n:
        ans.append(l)
        return
    
    for i in range(x+1,m+1):
        dfs(i,l+[i])

dfs(0,[])
for i in ans:
    print(*i)