n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
x = int(input())
mochi = [0]*(x+1)
for b in B:
    mochi[b] = 1

dp = [0]*(x+1)
dp[0] = 1
for i in range(x):
    if dp[i] == 0 or mochi[i]:
        continue
    for a in A:
        if i+a <= x:
            dp[i+a] = 1
print("Yes" if dp[-1] else "No")