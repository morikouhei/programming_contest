n = int(input())
XYZ = [list(map(int,input().split())) for i in range(n)]

Z = sum([z for _,_,z in XYZ])
inf = 10**20
dp = [inf]*(Z+1)
dp[0] = 0

for x,y,z in XYZ:
    need = max((x+y+1)//2-x,0)

    for i in range(Z)[::-1]:
        if dp[i] == inf:
            continue
        if i+z > Z:
            continue
        dp[i+z] = min(dp[i+z],dp[i]+need)


ans = min(dp[(Z+1)//2:])
print(ans)