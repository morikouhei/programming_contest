def solve():
    n = int(input())
    child = [list(map(int,input().split())) for i in range(n)]
    sweet = [list(map(int,input().split())) for i in range(n+1)]
    sweet = sweet[1:] + [sweet[0]]

    dist = []
    for i in range(n):
        x,y = child[i]
        l = []
        for nx,ny in sweet:
            d = (x-nx)**2+(y-ny)**2
            l.append(d)
        dist.append(l)
        print(*l)

    dp = [[0]*(1<<n) for i in range(1<<n)]
    dp[0][0] = 1
    last = [[0]*(1<<n) for i in range(1<<n)]
    for i in range(1<<n):
        for j in range(1<<n):
            if dp[i][j] == 0:
                continue
            for nind in range(n):
                if i >> nind & 1:
                    continue
                dm = 10**20
             
                for k in range(n+1):
                    if j >> k & 1:
                        continue

                    if dm > dist[nind][k]:
                        dm = dist[nind][k]
                for k in range(n):
                    if j >> k & 1:
                        continue
                    if dm == dist[nind][k]:
                        ni = i|1<<nind
                        nj = j|1<<k
                        if dp[ni][nj]:
                            continue
                        dp[ni][nj] = 1
                        last[ni][nj] = [nind,k]
                        
    
    if dp[-1][-1] == 0:
        return "IMPOSSIBLE"

    ans = []
    x,y = (1<<n)-1,(1<<n)-1
    while x != 0 or y != 0:
        nx,ny = last[x][y]
        ans.append([nx+1,ny+2])
        x ^= 1<<nx
        y ^= 1<<ny

    return ans[::-1]
    

                    

            

t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    if ans == "IMPOSSIBLE":
        print(ans)
        continue
    print("POSSIBLE")
    for i in ans:
        print(*i)
    
