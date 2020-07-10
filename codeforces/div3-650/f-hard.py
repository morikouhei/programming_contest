from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l2 = sorted(list(set(l)))
    
    d = defaultdict(int)
    ind = [[-1]*2 for i in range(len(l2))]
    num = [0]*len(l2)
    pos = [0]*len(l2)
    for i in range(len(l2)):
        d[l2[i]] = i

    cl = [-1]
    for i in range(n):
        x = d[l[i]]
        cl.append(x)
        num[x] += 1
        if ind[x][0] == -1:
            ind[x][0] = i+1
        ind[x][1] = i+1
    dp = [[0]*3 for i in range(n+1)]
    
    for i in range(1,n+1):
        x = cl[i]
        dp[i][0] = dp[pos[x]][0] + 1
        if x == 0:
            dp[i][1] = dp[pos[x]][1]+1
        else:
            dp[i][1] = max(dp[pos[x]][1],dp[pos[x-1]][0],dp[pos[x-1]][2])+1
        if i == ind[x][1]:
            dp[i][2] = dp[ind[x][0]][1]+num[x]-1
        pos[x] = i
    ans = 0
    
    for i in dp:
        ans = max(ans,max(i))
    print(n-ans)
