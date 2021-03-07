n = int(input())
A = list(map(int,input().split()))
l = [0]*4
for a in A:
    l[a] += 1

dp = [[[-1]*(l[3]+1) for i in range(l[2]+l[3]+1)] for j in range(n+1)]
dp[0][0][0] = 0
def dfs(c1,c2,c3):
    if dp[c1][c2][c3] >= 0:
        return dp[c1][c2][c3]
    count = n
    s = c1+c2+c3
    if c1 != 0:
        count += c1*dfs(c1-1,c2,c3)
    if c2 != 0:
        count += c2*dfs(c1+1,c2-1,c3)
    if c3 != 0:
        count += c3*dfs(c1,c2+1,c3-1)
    count /= s
    dp[c1][c2][c3] = count
    return count
print(dfs(l[1],l[2],l[3]))

