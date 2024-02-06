n = int(input())
D = list(map(int,input().split()))

inf = 10**20
l1,c1,k1 = map(int,input().split())
l2,c2,k2 = map(int,input().split())
dp = [-1]*(k1+1)
dp[k1] = k2
for d in D:
    ndp = [-1]*(k1+1)
    for i in range(k1+1):
        if dp[i] == -1:
            continue
        num = dp[i]
        for j in range(i+1):
            ni = i-j

            rest = max(d - j * l1,0)

            need = (rest+l2-1)//l2
            if need <= num:
                ndp[ni] = max(ndp[ni],num-need)

            if rest == 0:
                break

    dp = ndp

ans = inf
for i in range(k1+1):
    if dp[i] == -1:
        continue
    score = (k1-i)*c1 + (k2-dp[i])*c2
    ans = min(ans,score)

if ans == inf:
    ans = -1
print(ans)