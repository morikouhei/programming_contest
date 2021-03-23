n = int(input())
S = input()
X = input()

dp = [0]*7
dp[0] = 1
ten = 1
for i in range(n)[::-1]:
    ndp = [0]*7
    num = int(S[i])
    for j in range(7):
        nj = (num*ten+j)%7
        if X[i] == "T":
            ndp[j] = dp[j] | dp[nj]
        else:
            ndp[j] = dp[j] & dp[nj]

    dp = ndp
    ten = (ten*10)%7
print("Takahashi" if dp[0] else "Aoki")