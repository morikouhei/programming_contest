a,b = map(int,input().split())

prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

n = 20
n2 = 1<<n
dp = [0]*n2
dp[0] = 1

for i in range(a,b+1):
    s = 0
    for j,p in enumerate(prime):
        if i%p == 0:
            s |= 1<<j

    for j in range(n2):
        if s&j:
            continue
        dp[s|j] += dp[j]
print(sum(dp))