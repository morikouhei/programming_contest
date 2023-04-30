a,x,mod = map(int,input().split())


def calc(x,y):
    ans = [[0]*2 for i in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] += x[i][k]*y[k][j]
                ans[i][j] %= mod
    return ans


A = [[a,0],[a,1]]
base = [[1,0],[0,1]]
x -= 1

while x:
    if x%2:
        base = calc(A,base)
    x //= 2
    A = calc(A,A)
print(sum(base[1])%mod)