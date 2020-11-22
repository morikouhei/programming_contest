n = int(input())
c = [input() for i in range(4)]
if n == 2 or n == 3:
    print(1)
    exit()
mod = 10**9+7
if c[1] == "A" and c[0] == "A":
    print(1)
    exit()
if c[1] == "B" and c[3] == "B":
    print(1)
    exit()
if c[1] == "A" and c[2] == "B":
    print(pow(2,n-3,mod))
    exit()
if c[1] == "B" and c[2] == "A":
    print(pow(2,n-3,mod))
    exit()
dp = [1,1]
for i in range(n):
    dp.append((dp[-1]+dp[-2])%mod)
print(dp[n-2])