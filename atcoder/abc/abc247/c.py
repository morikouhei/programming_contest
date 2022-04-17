n = int(input())
def dfs(n):
    if n == 1:
        return [1]
    
    c = dfs(n-1)
    return c + [n] + c

print(*dfs(n))
