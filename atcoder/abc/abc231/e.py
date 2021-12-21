n,x = map(int,input().split())
A = list(map(int,input().split()))

dic = {}

def dfs(x,ind):
    if ind == 0:
        return x

    if (x,ind) in dic:
        return dic[(x,ind)]

    ans = x//A[ind]+dfs(x%A[ind],ind-1)
    ans = min(ans,x//A[ind]+1+dfs(A[ind]-(x%A[ind]),ind-1))
    dic[(x,ind)] = ans
    return ans

print(dfs(x,n-1))


