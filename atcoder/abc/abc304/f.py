n = int(input())
S = input()

mod = 998244353

ans = 0
divs = []
dp = []
for i in range(1,n):
    if n%i:
        continue

    divs.append(i)
    loop = i
    size = [0]*loop
    for j,s in enumerate(S):
        if s == ".":
            size[j%loop] = 1
    
    pat = 1
    for s in size:
        if s == 0:
            pat *= 2
            pat %= mod
    dp.append(pat)


for i in range(len(divs)):
    for j in range(i+1,len(divs)):
        if divs[j]%divs[i] == 0:
            dp[j] -= dp[i]
            dp[j] %= mod
print(sum(dp)%mod)