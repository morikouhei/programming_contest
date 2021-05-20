


T = int(input())
L = [int(input()) for i in range(T)]
M = max(L)
dp = [1]*(M+1)
l = [[] for i in range(M+1)]
for i in range(M+1):
    l[i].append(i)

for i in range(3,M+1):
    for cand in l[i]:
        for j in range(i+cand*2,M+1,cand):
            if dp[j] < dp[i]+1:
                dp[j] = dp[i]+1
                l[j] = [j-i]
            elif dp[j] == dp[i]+1:
                l[j].append(j-i)

for t in range(T):
    ans = dp[L[t]]
    print("Case #{}: {}".format(t+1,ans))
