
numl = [0]*n
resl = [0]*n
def dfs(x,pre):
    num = 0
    res = 1
    for nex in e[x]:
        if nex == pre:
            continue
        dfs(nex,x)
        num += numl[nex]
        res *= nCr(num,numl[nex],mod)*resl[nex]
        res %= mod
    numl[x] = num+1
    resl[x] = res
 
    return 
 
dfs(0,-1)
 
ans = [0]*n
ans[0] = resl[0]
def dfs2(x,pre):
    
    for nex in e[x]:
        if nex == pre:
            continue
        pres = [resl[x], numl[x], resl[nex], numl[nex]]
        resl[x] *= pow(nCr(numl[x]-1,numl[nex],mod)*resl[nex],mod-2,mod)
        resl[x] %= mod
        numl[x] -= numl[nex]
        resl[nex] *=  nCr(numl[x]+numl[nex]-1,numl[x],mod)*resl[x]
        resl[nex] %= mod
        numl[nex] += numl[x]
        ans[nex] = resl[nex]
        dfs2(nex,x)
        resl[x], numl[x], resl[nex], numl[nex] = pres
    return
dfs2(0,-1)
for i in ans:
    print(i)