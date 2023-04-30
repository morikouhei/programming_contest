h,w,t = map(int,input().split())
S = [list(map(int,input().split())) for i in range(h)]

cum = [[0]*(w+1) for i in range(h+1)]
for i in range(h):
    for j in range(w):
        cum[i+1][j+1] = S[i][j]

for i in range(h+1):
    for j in range(w):
        cum[i][j+1] += cum[i][j]

for i in range(w+1):
    for j in range(h):
        cum[j+1][i] += cum[j][i]


def get_area(a,b,c,d):

    return cum[c][d]+cum[a][b]-cum[c][b]-cum[a][d]


mins = set()
for h1 in range(h):
    for w1 in range(w):
        for h2 in range(h1,h):
            for w2 in range(w1,w):
                count = 0
                for x in range(h1,h2+1):
                    for y in range(w1,w2+1):
                        count += S[x][y]
                mins.add(count)



mins = sorted(mins)

inf = 10**20
ans = inf

size = 7**6

def id(a,b,c,d,x):

    return a*(7**5) + b*(7**4) + c*(7**3) + d*(7**2)+x

def solve(mi):
    dp = [inf]*size
    for i in range(t+1):
        for a in range(h):
            for b in range(w):
                for c in range(a+1,h+1):
                    for d in range(b+1,w+1):
                        if (c-a)*(d-b) < i:
                            continue

                        area = get_area(a,b,c,d)
                        if area < mi:
                            continue

                        pos = id(a,b,c,d,i)
                        if i == 0:
                            dp[pos] = area
                            continue
                        
                        num = inf
                        for ac in range(a+1,c):
                            pos1 = id(a,b,ac,d,0)
                            pos2 = id(ac,b,c,d,i-1)
                            for ni in range(i):
                                nex = max(dp[pos1],dp[pos2])
                                if nex < num:
                                    num = nex
                                pos1 += 1
                                pos2 -= 1

                        for bd in range(b+1,d):
                            pos1 = id(a,b,c,bd,0)
                            pos2 = id(a,bd,c,d,i-1)
                            for ni in range(i):
                                nex = max(dp[pos1],dp[pos2])
                                if nex < num:
                                    num = nex
                                
                                pos1 += 1
                                pos2 -= 1
                        
                        dp[pos] = num

    return dp[id(0,0,h,w,t)]-mi


for mi in mins:
    ans = min(ans,solve(mi))

print(ans)