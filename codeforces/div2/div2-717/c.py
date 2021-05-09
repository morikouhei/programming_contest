from math import gcd
n = int(input())
A = list(map(int,input().split()))
s = sum(A)
M = 2*10**5+1
dp = [0]*(M+5)
dp[0] = 1
g = A[0]
ind = 0
for a in A:
    g = gcd(a,g)
    for j in range(M)[::-1]:
        if j+a <= M:
            dp[j+a] |= dp[j]
if s%2 or dp[s//2] == 0:
    print(0)
    exit()
for i,a in enumerate(A,1):
    if (a//g)%2:
        print(1)
        print(i)
        exit()
