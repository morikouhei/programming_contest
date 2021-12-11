from functools import cmp_to_key

n,k = map(int,input().split())
S = [input() for i in range(n)]

def cmp(a,b):
    if  a+b < b+a:
        return 1
    return -1
S.sort(key= cmp_to_key(cmp))
dp = [""]*(k+1)
for s in S:
    for i in range(k)[::-1]:
        if i and dp[i] == "":
            continue
        if dp[i+1] == "":
            dp[i+1] = s+dp[i]
        elif s+dp[i] < dp[i+1]:
            dp[i+1] = s+dp[i]
print(dp[-1])
