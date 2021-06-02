n,m = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(m)]
dp = [0]*(2*m+10)
s = set()
for x,y in XY:
    s.add(x)
s = sorted(list(s))
dic = {x:i for i,x in enumerate(s)}

le = len(s)

lis = [[] for i in range(le+1)]
for x,y in XY:
    lis[dic[x]].append(y)

dp[m+1] = 1
mi = n-m-1
for i,l in enumerate(lis):
    upd = []
    for ind in l:
        if ind < n-m-1 or ind > n+m+1:
            continue
        if ind != 0 and dp[ind-mi-1] != 0:
            upd.append((ind-mi,1))
            continue
        if ind != 2*n and dp[ind-mi+1] != 0:
            upd.append((ind-mi,1))
            continue

        if dp[ind-mi] == 1:
            upd.append((ind-mi,0))

    for x,d in upd:
        dp[x] = d
print(sum(dp))