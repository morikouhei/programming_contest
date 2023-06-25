import sys
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())

vis = [0]*(n+1)
vis[1] = 1

def dfs(now,p):
    
    if now == n:
        s = input()
        exit()
    
    vis[now] = 1
    vs = list(map(int,input().split()))

    for v in vs[1:]:
        if vis[v]:
            continue
        print(v)
        sys.stdout.flush()
        dfs(v,now)

    print(p)
    sys.stdout.flush()
    vs = list(map(int,input().split()))
    return
    dfs(p,-1)

dfs(1,-1)
