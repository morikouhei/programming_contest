X = int(input())
mod = 998244353

dic = {}
def dfs(x):
    if x in dic:
        return dic[x]
    a = x//2
    b = (x+1)//2
    if a*b <= x:
        return x

    dic[x] = dfs(a)*dfs(b)%mod
    return dic[x]

print(dfs(X))