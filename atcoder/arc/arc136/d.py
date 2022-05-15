n = int(input())
A = list(map(int,input().split()))
M = 10**6
dp = [0]*M
for a in A:
    dp[a] += 1

for t in range(6):
    nten = 10**(t+1)
    ten = 10**(t)
    for i in range(M):
        if i//ten%10 == 9:
            continue
        dp[i+ten] += dp[i]

ans = 0
for a in A:
    l = []
    now = a
    for i in range(6):
        l.append(str(9-now%10))
        now //= 10

    cand = int("".join(l[::-1]))
    ans += dp[cand]
    ins = 1
    now = a
    for i in range(6):
        if now%10 > cand%10:
            ins = 0
        now //= 10
        cand //= 10
    ans -= ins
print(ans//2)
