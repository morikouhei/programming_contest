n,k = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]
mod = 10**9+7

def cal(x,y):
    ans = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += x[i][k]*y[k][j]
                ans[i][j] %= mod
    return ans

ans = [[0]*n for i in range(n)]
for i in range(n):
    ans[i][i] = 1


while k:
    if k%2:
        ans = cal(ans,A)
    A = cal(A,A)
    k //= 2
count = 0
for i in ans:
    for j in i:
        count += j
        count %= mod
print(count)

